from typing import List, Any

import tensorflow as tf
import numpy as np


# TODO незаконченная часть проекта
# Данный код не является рабочим и оставлен для будущих доработок

def convert_to_tf_lite_with_quantization(model_path, tf_lite_module_output_path):
    converter = tf.lite.TFLiteConverter.from_saved_model(model_path)
    converter.optimizations = [tf.lite.Optimize.DEFAULT]
    converter.target_spec.supported_ops = [
        tf.lite.OpsSet.TFLITE_BUILTINS,
        tf.lite.OpsSet.SELECT_TF_OPS
    ]

    tflite_quant_model = converter.convert()

    with open(f"{tf_lite_module_output_path}.tflite", "wb") as f:
        f.write(tflite_quant_model)



class TfLiteModel:
    @classmethod
    def from_file(cls, model_path):
        return TfLiteModel(tf.lite.Interpreter(model_path=model_path))

    @classmethod
    def from_keras_model(cls, kmodel):
        converter = tf.lite.TFLiteConverter.from_keras_model(kmodel)
        tflite_model = converter.convert()
        return TfLiteModel(tf.lite.Interpreter(model_content=tflite_model))

    def __init__(self, interpreter):
        self.interpreter = interpreter
        self.interpreter.allocate_tensors()

        self.input_details = interpreter.get_input_details()
        self.output_details = interpreter.get_output_details()
        self.input_shape = self.input_details[0]['shape']
        self.input_tensor_index = self.input_details[0]['index']
        self.output_tensor_index = self.output_details[0]['index']
        self.input_dtype = self.input_details[0]["dtype"]

    def predict_single(self, input_data_for_single_observation):
        input_data = input_data_for_single_observation.astype(self.input_dtype)
        self.interpreter.set_tensor(self.input_tensor_index, input_data)

        self.interpreter.invoke()

        return self.interpreter.get_tensor(self.output_details[0]['index'])

    def predict(self, input_data_for_many_observations: List[List]):
        result = []

        for input_data_for_single_observation in input_data_for_many_observations:
            result.append(self.predict_single(input_data_for_single_observation))

        return result
