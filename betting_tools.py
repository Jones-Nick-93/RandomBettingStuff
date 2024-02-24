#!/usr/bin/env python
# coding: utf-8

# In[27]:


#turn the probability from a simulation into decimal odds price
def implied_probability_to_decimal_odds(implied_probability):
    # Ensure the implied probability is between 0 and 1
    if not (0 <= implied_probability <= 1):
        raise ValueError("Implied probability must be between 0 and 1.")

    # Convert implied probability to decimal odds
    decimal_odds = round(1 / implied_probability, 2)
    
    return decimal_odds

# Example usage:
implied_prob = float(input("Enter the implied probability (as a decimal): "))
decimal_odds = implied_probability_to_decimal_odds(implied_prob)
print("Equivalent Decimal Odds:", decimal_odds)


# In[26]:


#turning american odds price to decimal
def american_to_decimal(odds):
    if odds < 0:
        return 100 / abs(odds)
    elif odds > 0:
        return odds / 100
    else:
        return 1
#calculating staking size using quarter kelly criterion staking
def calculate_bet_size():
    try:
        pairs = []
        while True:
            try:
                american_odds = float(input("Enter the American odds received on the bet (or enter any non-numeric value to finish): "))
                
                if not american_odds:
                    break

                win_probability = float(input("Enter the estimated probability of winning (as a decimal): "))
                pairs.append((american_odds, win_probability))
            except ValueError:
                print("Invalid input. Please enter valid numerical values.")

        for american_odds, win_probability in pairs:
            # Convert American odds to decimal odds
            decimal_odds = american_to_decimal(american_odds)

            # Calculate q (probability of losing)
            lose_probability = 1 - win_probability

            # Calculate f* (Kelly Criterion)
            f_star = (decimal_odds * win_probability - lose_probability) / decimal_odds

            # Calculate f (1/4 Kelly Criterion)
            f = 1/4 * f_star

            # Convert f to percentage
            bet_size_percentage = f * 100

            print("For American Odds {}, Win Probability {:.2%}, Recommended bet size: {:.2f}%".format(
                american_odds, win_probability, bet_size_percentage))

    except ValueError as e:
        print(f"Error: {e}. Please enter valid numerical values.")

# Example usage:
calculate_bet_size()


# In[31]:


#generating american odds price from input sim probabilities
def percent_to_price():
    num_probabilities = int(input("Enter the number of probabilities: "))
    implied_probabilities = [float(input(f"Enter probability {i + 1}: ")) for i in range(num_probabilities)]

    american_odds_list = []
    for implied_probability in implied_probabilities:
        if 0 < implied_probability <= 1:
            odds_decimal = 1 / implied_probability
            if odds_decimal < 2:
                american_odds = int(-(100 / (odds_decimal - 1)))
            else:
                american_odds = int(odds_decimal * 100 - 100)
            american_odds_list.append(american_odds)
        else:
            raise ValueError("Implied probability must be between 0 and 1 (exclusive)")

    return american_odds_list

# Example usage:
fair_prices = percent_to_price()
print("Odds for each probability:", fair_prices)


# In[32]:


percent_to_price()


# In[ ]:




