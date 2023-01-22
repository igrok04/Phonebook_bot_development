# import data_generation as dg
import user_interface as ui
import logger as lg
import crud
import os
os.chdir(os.path.dirname(__file__))


# dg.start() # генерация базы контактов
lg.logging.info('Start')
crud.init_data_base('base_phone.csv')
ui.ls_menu()
