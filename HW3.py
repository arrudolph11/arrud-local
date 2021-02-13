# Your name: Amanda Rudolph
# Your student id: 87253704
# Your email: arrud@umich.edu
# List who you have worked with on this homework:


# import the random module for use in this program
import random

# Create the class Magic_8
class Magic_8:
    def __init__(self, answer_list): 
        self.answer_list = answer_list
        self.question_list = []
        self.answer_history_list = []
    
    def __str__(self):
        return ",".join(self.answer_list)

    def shake_ball(self):
        randIndex = random.randint(0, (len(self.answer_list) -1))
        self.answer_history_list.append(randIndex)
        return self.answer_list[randIndex]

    def check_question(self, question):
        if question in self.question_list:
            return "I already answered that question!"
        else:
            self.question_list.append(question)
            return self.shake_ball()

    def print_history(self):
        if self.answer_history_list == []:
            print("None yet")
        else:
            for i in range(len(self.answer_history_list)):
                answer_index = self.answer_history_list[i]
                print("[" + str(answer_index) + "] " +  self.question_list[i])
            
    # EXTRA POINTS
    # create the generate_n_responses method
    # it takes as input:
    #    a number, n. Ex: 200
    # it generates a random response n times by calling shake_ball
    # then returns the index and length of the longest consecutive run
    # It should reset the answer_history_list to an empty list first. 
    # A run is a repetition of the same number consecutively in a list.
    # Ex: If 10 random answers are  [1,5,6,3,2,4,1,4,4,4] then three 4's is the longest run
    # hence the function should return "longest run was length of 3 for index 4
    
def main():
    answer_list = ["Yes", "No", "Ask again", "Maybe", "Not clear"]
    bot = Magic_8(answer_list)
    while True:
        userInput = input("Enter question or 'quit': ")
        if userInput == 'quit':
            break
        else: 
            answer = bot.check_question(userInput)
            print(f" {userInput} - {answer}")


def test():
    
    answer_list = ["Yes", "No", "Ask again", "Maybe", "Not clear"]

    print()
    print("Testing Magic 8 Ball:")
    bot2 = Magic_8(answer_list)

    print("Testing the __str__ method")
    print(bot2)
    print()

    print("Printing the history when no answers have been generated yet")
    bot2.print_history()
    print()

    print("Asking the Question: Am I hungry?")
    print(bot2.check_question("Am I hungry?"))
    print()

    print("Asking the Question: Am I hungry? again")
    print(bot2.check_question("Am I hungry?"))
    print()

    print("Asking the Question: Should I go for a walk?")
    print(bot2.check_question("Should I go for a walk"))
    print()

    print("Printing the history")
    bot2.print_history()
    print()
    
    #EXTRA POINTS
    #Uncomment the lines below if you attempt the extra credit!
    #print("Testing generate_n_responses method with 200 responses")
    #print(bot2.generate_n_responses(200))


# only run the main function if this file is being run (not imported)
if __name__ == "__main__":
    main()
    #test() - uncomment when you are ready to test your magic 8 ball
