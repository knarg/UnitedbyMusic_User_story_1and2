def main():
    import json
    print("You are about to unite with people under the aim of music")
    # Opening my dicrtionary that has one question only ( please refer to the other file to see it )
    with open('my_dict.json') as f:
        dict = json.load(f)

    # prompting the user to input the required details

    print("Please choose number from the following:")
    print("1 : Ask new Question")
    print("2 : See the previously asked questions")
    print("3 : Answer existing question")

    user_input= int(input())


    if user_input == 1:

        # taking the user question

        user_ask = input("what is your question?")

        #Adding the question at the end of our list of questions

        dict[int(len(dict.keys())+1)]=  {user_ask:""}

        # saving it as json file

        with open('my_dict.json', 'w') as f:
            json.dump(dict, f)

    elif user_input == 2:
        # loading the json file to view the latest questions

        with open('my_dict.json') as f:
            dict = json.load(f)

        print(dict)

    elif user_input == 3:

        # loading the json file to show the questions that need to be answered

        with open('my_dict.json') as f:
            dict = json.load(f)

        print(dict)

        #getting the required detailes

        question_number = int(input('number of question ? '))
        user_question = input(" Plase Insert the question you will answer ")
        user_answer = input("Please Insert your answer?")

        # updating the asnwer to the question by removing the preview one and adding this one

        dict[question_number] = {user_question:user_answer}

        #saving the changes to json file to be viewed later

        with open('my_dict.json', 'w') as f:
            json.dump(dict, f)
    else :
        print("Please type as required")
        exit

main()