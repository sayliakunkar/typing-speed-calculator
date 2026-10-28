import time
import random

sentences = [
    "The quick brown fox jumps over the lazy dog.",
    "A journey of a thousand miles begins with a single step.",
    "To be or not to be, that is the question."
]

def measure_accuracy(use_input, sentence):
    correct_chars = sum(1 for a, b in zip(use_input, sentence) if a == b)
    accuracy = (correct_chars / len(sentence)) * 100
    return accuracy

def typing_test():
    sentence = random.choice(sentences)
    print("Type the following sentence:")
    print(sentence)

    
    input("Press Enter when you're ready to start...")
    start_time = time.time() #measure the start time
    user_input = input("Your input: ")
    end_time = time.time() #measure the end time
    time_taken = end_time - start_time #calculate the time taken
    time_taken_in_minutes = time_taken / 60 #convert time taken to minutes
    word_count = len(user_input.split(" ")) #count the number of words typed

    print("Results:")
    print(f"Time taken: {time_taken_in_minutes:.2f} seconds")
    print(f"Words typed: {word_count}") 
    print(f"Typing speed: {word_count / time_taken_in_minutes:.2f} words per minute")
    accuracy = measure_accuracy(user_input, sentence)
    print(f"Accuracy: {accuracy:.2f}%") 
    
typing_test()