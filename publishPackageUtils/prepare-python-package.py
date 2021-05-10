import os

PUBLISH_UTILS_FOLDER = 'publishPackageUtils'
TEMP_PUBLISH_FOLDER = 'tempPublishFolder'
PACKAGE_NAME = 'toxic-comments-detector'

remove_old_package_dist = f'rm -rf ./{TEMP_PUBLISH_FOLDER}'
create_new_package_dist = f'mkdir {TEMP_PUBLISH_FOLDER}'

copy_text_preprocessing_folder = f'cp -R textPreprocessing {TEMP_PUBLISH_FOLDER}/{PACKAGE_NAME}/'
copy_dev_folder = f'cp -R dev {TEMP_PUBLISH_FOLDER}/{PACKAGE_NAME}/'
copy_navec = f'cp wordEmbeddingsLayers/navec/navec_vectorizer_layer.py {TEMP_PUBLISH_FOLDER}/{PACKAGE_NAME}/ && cp wordEmbeddingsLayers/navec/navecWeights.tar {TEMP_PUBLISH_FOLDER}/{PACKAGE_NAME}/'
copy_final_model = f'cp {PUBLISH_UTILS_FOLDER}/final_model.py {TEMP_PUBLISH_FOLDER}/{PACKAGE_NAME}/ && cp -R .savedModels/weightedCNN_NavecWordEmbeddings {TEMP_PUBLISH_FOLDER}/{PACKAGE_NAME}/ && cp {PUBLISH_UTILS_FOLDER}/__init__.py {TEMP_PUBLISH_FOLDER}/{PACKAGE_NAME}/'
copy_files_for_package_publish = f'cp {PUBLISH_UTILS_FOLDER}/setup.py {TEMP_PUBLISH_FOLDER}/ && cp {PUBLISH_UTILS_FOLDER}/setup.cfg {TEMP_PUBLISH_FOLDER}/ && cp {PUBLISH_UTILS_FOLDER}/README.md {TEMP_PUBLISH_FOLDER}/'

commands_order = [
    remove_old_package_dist,
    create_new_package_dist,
    copy_text_preprocessing_folder,
    copy_dev_folder,
    copy_navec,
    copy_final_model,
    copy_files_for_package_publish,
]

for command in commands_order:
    os.system(command)
