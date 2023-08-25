import logging
from pydantic import BaseModel

logger = logging.getLogger(__name__) # Indicamos que tome el nombre del modulo
logger.setLevel(logging.DEBUG) # Configuramos el nivel de logging
formatter = logging.Formatter('%(asctime)s:%(name)s:%(module)s:%(levelname)s:%(message)s') # Creamos el formato
file_handler = logging.FileHandler('api_main.log') # Indicamos el nombre del archivo
file_handler.setFormatter(formatter) # Configuramos el formato
logger.addHandler(file_handler) # Agregamos el archivo

class Stroke(BaseModel):
    """
    Represents a passenger on the Titanic with various attributes.
    
    Attributes:
        pclass_nan (float): Placeholder for missing values in 'pclass' attribute.
        age_nan (float): Placeholder for missing values in 'age' attribute.
        sibsp_nan (float): Placeholder for missing values in 'sibsp' attribute.
        parch_nan (float): Placeholder for missing values in 'parch' attribute.
        fare_nan (float): Placeholder for missing values in 'fare' attribute.
        sex_male (float): Placeholder for 'sex' attribute being male.
        cabin_Missing (float): Placeholder for 'cabin' attribute being missing.
        cabin_rare (float): Placeholder for 'cabin' attribute being rare.
        embarked_Q (float): Placeholder for 'embarked' attribute being Queenstown.
        embarked_S (float): Placeholder for 'embarked' attribute being Southampton.
        title_Mr (float): Placeholder for 'title' attribute being Mr.
        title_Mrs (float): Placeholder for 'title' attribute being Mrs.
        title_rar (float): Placeholder for 'title' attribute being rare.
    """

    age: float
    hypertension: int  
    heart_disease: int  
    avg_glucose_level: float
    bmi: float
    age_nan: int  
    avg_glucose_level_nan: int  
    bmi_nan: int  
    hypertension: int  
    heart_disease: int  
    gender_Male: bool   
    ever_married_Yes: bool   
    work_type_Never_worked: bool   
    work_type_Private: bool
    work_type_Self_employed: bool	
    work_type_children: bool	
    Residence_type_Urban: bool
    smoking_status_formerly_smoked: bool
    smoking_status_never_smoked: bool   
    smoking_status_smokes: bool