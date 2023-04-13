from flask import *
import json, time 
import random




app = Flask(__name__)



@app.route('/',methods=['GET'])
def home_page():
    
    data_set = { 'Message': 'Successfully Loaded the Home page', 'Timestamp':time.time(),
                 '/random_question':'To Fetch a Random Question',
                 '/total_question':'To Fetch all Question',
                 '/selected_question':'To Fetch a Range of Question'
                }
    
    jason_dump = json.dumps(data_set)
    
    return jason_dump

@app.route('/random_questions/',methods=['GET'])
def questions_page():
    
    with open('questions.txt','r') as f:
        data = f.readlines()
        random_number = random.randrange(0, 120, 6)
        question = data[random_number].replace('\n'," ")
        option1 = data[random_number+1].replace('\n'," ")
        option2 = data[random_number+2].replace('\n'," ")
        option3 = data[random_number+3].replace('\n'," ")
        option4 = data[random_number+4].replace('\n'," ")
    
    data_set = {'Question':f'{question}',
                'Option 1':f'{option1}',
                'Option 2':f'{option1}',
                'Option 3':f'{option1}',
                'Option 4':f'{option1}',
                }
    jason_dump = json.dumps(data_set)
    
    return jason_dump

    

@app.route('/total_questions/', methods=['GET'])
def request_page(): 
    
    response = ''
    try:
        with open('questions.txt', 'r') as f:
            data = f.readlines()
            response = 0
        return  data , response
    except FileNotFoundError:
        response = 1
        return 'File not found', response
    except Exception as e:
        response = 2
        return str(e), response
    finally: 
        
        else_data = []
        for i in range(0,len(data),6): 
            else_data.append({'Options':f'{data[i+1]},{data[i+2]},{data[i+3]},{data[i+4]}'.replace('\n',''),'Questions': f'{data[i]}'.replace('\n',''),'Correct Answer': f'{data[i+1]}'.replace('\n','')})
        
        data_set = { 'Code Response': f'{response}', 'Data':f'{else_data}'}
        jason_dump = json.dumps(data_set)
        
        return jason_dump
                    

@app.route('/selected_questions/', methods=['GET'])
def request_question_page(): 
    
    response = ''
    try:
        with open('questions.txt', 'r') as f:
            data = f.readlines()
            response = 0
        return  data , response
    except FileNotFoundError:
        response = 1
        return 'File not found', response
    except Exception as e:
        response = 2
        return str(e), response
    finally: 
        
        user_query = str(request.args.get('number')) #/questions/?number=10            
        
        if int(user_query)>20 or int(user_query)<0:
            
            data_set = { 'Code Response': f'{2}', 'Message':'Exceed Questions Limit'}
            jason_dump = json.dumps(data_set)
        
            return jason_dump
            
        elif user_query :    
            new_data = []
            count = 1
            for i in range(1,len(data),6):
            
                if count <= int(user_query):
                    new_data.append({'Options':f'{data[i+1-1]},{data[i+2-1]},{data[i+3-1]},{data[i+4-1]}'.replace('\n',''),'Questions': f'{data[i-1]}'.replace('\n',''),'Correct Answer': f'{data[i+1-1]}'.replace('\n','')})
                count += 1                 
            data_set = { 'Code Response': f'{response}', 'Data':f'{new_data}'}
            jason_dump = json.dumps(data_set)
            
            return jason_dump
                        
if __name__ == '__main__':
    app.run(port=7777)
    