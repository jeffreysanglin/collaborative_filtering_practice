#Adapted from Jeremy and FastAI
from pathlib import Path
from os import environ
from subprocess import check_call
from sys import executable
from pandas import read_csv

class KaggleUtil:
    def __init__(self, contest, credentials):
        self.contest = contest
        self.path = Path(contest)
        self.iskaggle = environ.get('KAGGLE_KERNEL_RUN_TYPE', '')
        
        def install_package(package):
            check_call([executable, "-m", "pip", "install", package])
        
        cred_path = Path('~/.kaggle/kaggle.json').expanduser()
        if not cred_path.exists():
            cred_path.parent.mkdir(exist_ok=True)
            cred_path.write_text(credentials)
            cred_path.chmod(0o600)
        
        if not self.iskaggle and not self.path.exists():
            import zipfile,kaggle
            kaggle.api.competition_download_cli(str('titanic'))
            zipfile.ZipFile(f'{self.path}.zip').extractall(self.path)

        if self.iskaggle:
            self.path = Path(f'../input/{contest}')
            #!pip install -q datasets
            install_package("datasets")
    
    def read_datasets(self, file_format=".csv"):
        if file_format==".csv":
            training_path = Path(f"{self.path}/train{file_format}")
            testing_path = Path(f"{self.path}/test{file_format}")
            training_set = read_csv(training_path)
            testing_set = read_csv(testing_path)
        return(training_set, testing_set)
        
    
    
    





    

