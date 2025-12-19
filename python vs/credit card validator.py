sum_odd_digit=0
sum_even_digit=0
total=0

# step 1
card_number=input("Enter a credit card number: ")
card_number=card_number.replace("-"," ")
card_number=card_number.replace(" ","")
card_number=card_number[::-1]

# Step 2
for i in card_number[::2]:
    sum_odd_digit+=int(i)

#step 3
for i in card_number[1::2]:
    i=int(i) *2
    if i > 9:
        sum_even_digit +=(1+(i%10))
    else:
        sum_even_digit += i

# step 4
total = sum_even_digit + sum_odd_digit

# step 5
if total % 10==0:
    print("valid")
else:
    print("invalid")
