# Write a program that asks the user for their age and their favorite movie.
# Then, it calculates the price of a movie ticket based on the age they entered:

# Ages 0-4: Free
# Ages 5-12: $7
# Ages 13-60: $10
# Ages 61+: $6
# The program should also keep track of all the favorite movies entered
# and print them at the end along with the total ticket price.

# The program should:

# Continuously ask for the user's age and favorite movie until the user
# enters 'done' for age.
# Handle non-integer input for age gracefully
# (ask again if the input isn't valid).
# After 'done' is entered, output total price and the list of favorite movies.

# First ask for age.
age_prompt = "\nEnter your age. "

# Then ask for their favorite movie.
movie_prompt = "\nWhat's your favorite movie? "

# A way to stop the loop.
end_prompt = "\nEnter 'done' when you finish. "

total_price = 0  # To store the total price of the movies.

while True:
    age_input = input(age_prompt + end_prompt)
    if age_input == 'done':  # Check if the user enter 'done' before converting
        break                     # to an integer.

    try:
        age = int(age_input)  # Convert age in an integer.
    except ValueError:        # Handle invalid age (string).
        print("Please enter a valid age.")
        continue

    movie_input = input(movie_prompt)  # Ask for a movie after age is provided.
    print(f"\nGreat choice! You like {movie_input.title()}!")

    if age < 5:
        ticket_price = 0
    elif age < 13:
        ticket_price = 7
    elif age < 61:
        ticket_price = 10
    else:
        ticket_price = 6

    total_price += ticket_price
print(f"\nThe total price of the movie tickets is ${total_price}")



