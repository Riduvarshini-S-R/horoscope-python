# Program which tells future based upon the zodiac sign

next = True
while next == True:
    print(''' From all the mentioned Zodiac Signs
    1) Aries
    2) Tauras
    3) Gemini
    4) Cancer 
    5) Leo
    6) Virgo
    7) Libra
    8) Scorpio
    9) Sagittarius
    10) Capricorn
    11) Aquarius
    12) Pisces
    ''')

    s = int(input("Enter your sign number to know your future\n"))


    if s==1:
        print("Limited capital will not prove an obstacle in putting a project on the road. Support of family members is assured in whatever you undertake.")
    elif s==2:
        print("A new source of income is likely to open up and promises to make you financially secure. Fitness mantra of a friend will do wonders for your health. ")
    elif s==3:
        print("You will need to remain guarded, as you may be taken for a ride on the monetary front. Things that were going wrong on the work front will begin to improve. ")
    elif s==4:
        print("You will benefit by taking a break from your regular exercise routine. Child or sibling may make you proud by his or her achievements. It will be prudent to keep a watchful eye on a business colleague. ")
    elif s==5:
        print("A bad cold or some other small ailment may trouble on and off. A family member studying out of town or abroad may become a source of worry.")
    elif s==6:
        print(" An exciting time in a family gathering is foreseen. Avoid offending someone by your actions at work. Money well spent may give you inner satisfaction. ")
    elif s==7:
        print("Your sympathetic touch will alleviate the problems of a family elder. Consistent performance will pave the way for promotion.")
    elif s==8:
        print(" Getting your money back from someone may require efforts, but get back, you will! Less work will enable you to take some time off for yourself. ")
    elif s==9:
        print("A property issue is likely to be resolved amicably. Performing well on the academic front will not pose much difficulty for you.")
    elif s==10:
        print("Something that is available on the house will help you save money. Some of you will have to adopt measures to blunt the impact of a lifestyle disease.")
    elif s==11:
        print("Unnecessarily worrying about your health will serve no purpose. A difference of opinion with the elders may make you ponder about something in mind. ")
    elif s==12:
        print("Watch your step on the financial front, as someone may sweet-talk you out of money. Putting off work for some other day will just not work on the professional front.")
    else:
        print("Hey You sure about the number?")

    next = True if input("\nShall we do it again? (Y/N) ")=="Y" else False
