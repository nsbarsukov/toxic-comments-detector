import os

PUBLISH_UTILS_FOLDER = 'publishPackageUtils'
PACKAGE_DIST_FOLDER = 'toxic-comments-detector'

remove_old_package_dist = f'rm -rf ./{PACKAGE_DIST_FOLDER}'
create_new_package_dist = f'mkdir {PACKAGE_DIST_FOLDER}'

copy_text_preprocessing_folder = f'cp -R textPreprocessing {PACKAGE_DIST_FOLDER}/'
copy_dev_folder = f'cp -R dev {PACKAGE_DIST_FOLDER}/'
copy_navec = f'cp wordEmbeddingsLayers/navec/navec_vectorizer_layer.py {PACKAGE_DIST_FOLDER}/ && cp wordEmbeddingsLayers/navec/navecWeights.tar {PACKAGE_DIST_FOLDER}/'
copy_final_model = f'cp {PUBLISH_UTILS_FOLDER}/final_model.py {PACKAGE_DIST_FOLDER}/ && cp -R .savedModels/weightedCNN_NavecWordEmbeddings {PACKAGE_DIST_FOLDER}/ && cp {PUBLISH_UTILS_FOLDER}/__init__.py {PACKAGE_DIST_FOLDER}/'
copy_file_for_package_publish = f'cp {PUBLISH_UTILS_FOLDER}/setup.py {PACKAGE_DIST_FOLDER}/ && cp {PUBLISH_UTILS_FOLDER}/setup.cfg {PACKAGE_DIST_FOLDER}/ && cp {PUBLISH_UTILS_FOLDER}/README.md {PACKAGE_DIST_FOLDER}/'

commands_order = [
    remove_old_package_dist,
    create_new_package_dist,
    copy_text_preprocessing_folder,
    copy_dev_folder,
    copy_navec,
    copy_final_model,
    copy_file_for_package_publish,
]

for command in commands_order:
    os.system(command)
