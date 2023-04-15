# from dotenv.main import load_dotenv
import os
load_dotenv()
HOST=os.environ['HOST']
USERNAME=os.environ['USERNAME']
PASSWORD=os.environ['PASSWORD']
DATABASE=os.environ['DATABASE']


master_db=f"mysql+mysqlconnector://{USERNAME}:{PASSWORD}@{HOST}/{DATABASE}"