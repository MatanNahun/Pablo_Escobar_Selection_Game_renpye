

# Declare characters used by this game. The color argument colorizes the
# name of the character.


define g = Character("Gustavo")
define p=Character("you")
define martino=Character("martino")


# The game starts here.

label start:
    $ life = 1
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene main2
    #show youwin with easeinright
    play music "music1.mp3"

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.




    g-"-Hello , Anyone there?"
    menu:
        "yes Im here":
            jump option1
        "No ":
            "do u think its another stupid game ah? Get ready smarty! "
            jump option1


    label option1:
    show gustaonew with easeinright
    g-" Amazing ,My name is Gustavo Gaviria , And I need your help! Let me explain, 17 years ago people thought I died and here I am back, No one knows about me anything except you so please keep it secret!. I promise it will pay off for you and ill explain more soon but we need to hurry Are u in?"

    $ name = renpy.input("what is your name")
    if name == "":
        "please tell me you name "

    menu:
        "yes I'm in ,tell me what's happening ":
            g-"Perfect [name]! Let me tell u my story In 1993 , I survived the gunshots from the police  back then "
            g-"I was found by a poor women near the Medellín city, she took care of me all this time in a small cave in rio claro to not be caught by the police ,"
            g-"you are probably wondering why I’m be traced by the police so let me explain , i am pablo escobar best friend and cousin ,  yeah the drug trafficker . If you don’t already know me,we were closer than brothers; we  grew up together and were partners from the beginning"
            g-"Me and Pablo our goal was always to make a lot of money so our small business turned to being   criminal by smuggling cigarettes and consumer electronics along with Pablo"
            g-" Afterwards the cocaine business started . I’m not going to exaggerate however I was the brain for all of our business which was worth around 59 billion dollars . I knew all the labs , where I should get the materials and chemicals , the transportation routes and distribution hubs in the USA and Europe ."
            g-" However the money we got was only in Pablo's hand ,no one  knew anything about where he was keeping it.In December 1993 , me and pablo tried to escape from the jail It wasn our first time trying. We had a plan however ,I managed to survive but he didn’t and was shot by the police to death."
            g-"Now I want to get our money back I have a deal for you, u help to find the money and i'll share it with you. Do you accept my offer?  "
    $life=2
    label one:
    menu:
        "No. im calling the cops":
            $life=life-1 # 1 life left
            g-"It was a mistake contacting you!! You just lost a big chance of becoming a billionaire for the rest of your life, you are now arrested  "
            g-"  1 WEEK LATER"
            g-"Because everyone deserves a second chance I’m giving you the chance to come back to life and help me find the money you are the bravest and most valuable person ,i've heard alot about you [name], I need you as much as you need me , so let's work together on becoming the wealthiest in this whole universe Do you accept this lifetime chance"
            jump one
        "yes lets do it! what's the plan":
            $ choice="1"
            jump option2
        "can i call a friend for help ?":
            jump option3
    if choice==1:
        label option2:
        g-"First you should know, its gonna be a dangerous mission and not that easy, i need u focus and sharp.Second, I have a connection with the police but we can use it just once! Use it carefully. Good, now listen carefully for every step that i will tell you.Few minutes after Pablo shot I found in his pocket a note with information about where Pablo had hidden the money, but he wrote it in a way that just Pablo will understand. Because I am his best friend and his close business partner. I understand some of it and I think it's enough to find the money . First step we need to find a key that Pablo buried next to his house. I can't go with you. It's too dangerous for me"
    else:
        label option3:
            g-" it's a secret you idiot! No one knows about me except you and a dead poor women,First you should know, its gonna be a dangerous mission and not that easy, i need u focus and sharp.Second, I have a connection with the police but we can use it just once! Use it carefully. Good, now listen carefully for every step that i will tell you.Few minutes after Pablo shot I found in his pocket a note with information about where Pablo had hidden the money, but he wrote it in a way that just Pablo will understand. Because I am his best friend and his close business partner. I understand some of it and I think it's enough to find the money . First step  we need to find a key that Pablo buried next to his house. I can't go with you. It's too dangerous for me "
    menu:
        "What is this key ? how is it going to help ?":
            g-"This key should open a safe in the central museum ,so because the museum has a really tough security Pablo Ascobar took advantage of it. He knew that no one would think that the money was there  , so he decided to hide his money in one of the safes at the central  museum "
        "Okay tell me where to go":
            g-"You are going  to find the key that will open a safe box in the central  museum"
    g-"I have the address for pablo's house the area is pretty isolated so let me know how you prefer to go there ?"
    menu :
        "Hitchhiking":
            jump option4
        "I'll take my car":

            jump option5

    label option4:
    g-"OKAY! But stay safe which driver you prefer (choose wisely):"
    menu:
            "Psycho driver":
                g-"Wooooof, he almost took me to the police this psycho. We r lucky"
            "the fancy car":
                "*The fancy car stopped in the middle of the road in an isolated place what should you do"
    menu:
        "CALL GUSTAVO for help ":
             g-"*Ring ring * All good?"
             "[name] :I need your help got stuck in the road"
             g-" after 15 min the car will be there  "


        "I will manage all by myself":
            g-"Okay but stay safe in this isolated area a lot of robbers in the way , we have to be connected all the time "

        "wait for a passing car for a drive":
             g-"Waited for more than 4  hours no one passed by , then all of a sudden an old man came by it was all blurry you barely see anything ,He came by you , there you were terrified ,but you were brave enough to ask him, “how can I get to the famous pablo’s house ?”The old man was terrified , his face was indescribable , he changed from the moment you said pablo’s name ,He run away you followed him because you felt he was your only chance to leave this isolated area ,  in order to cover the real story which is (gustavo) .You told him you came from a really far place just to see the place where the lord of drugs you made this up that you need a drive to his house to see it since you came all the way to here now . The old man then felt the need of helping you  ,so he told you Look ,I suggest you to walk there at this time of the day barely any car or taxi pass by either you wait in this cold weather for hours or i can walk you through to his house since i live 500 meter away from pablo's house "




    label option5:
    g-"Police stopped you at the middle of the road and call you to pull over"
    menu:
        "You pull over and act like nothing happens  ": #PROBLEM
            " the police arrested you for investigation and you lost a life"
            $life= life -1
            if life == 0:
                jump gameOver
            elif life == 1:
                g-"u lost life  - try to save your last life for us to get the money"
                jump yard
        " Run away!!!!":
            "your car is faster then the police and let u go"
            jump yard

    label gameOver:
    g-"you lost all your lives -game over"
    return

    label yard:
    g-"Ring ring"
    g-"Yo Ganvio i’m here. Fuck its a big house Good.now focus. it is supposed to be there next to his house. It is written that it's buried in a place that was close to his heart . Which is still complicated to understand.But as i know Pablo I suspicious that he meant to one of those three,I say start with the statue of himself in the living room ,now knock the door and good luck finding it!!"
    g-"You are cut off, no signal !!What is happening: "

    menu:
        "Just go directly inside the house":
            "The police are here shit !! fucklose connections/game over"
            $life=life-1
            if life==0:
                jump gameOver
            else :
                "you lost a life be careful "

        "the window in the living room to be safe":
            g-"A girl called anastasia was looking over the window "
            g-"Gustavio:That's his daughter Anastasia inside! I can't believe she is alive too! maybe she know something that can help  Tell her you were a good friend of her dad but remember don’t say shit about me! It will put her in a danger too, maybe she can give you a clue that will help us What Clue are you taking to look for the key :"
            jump comehere
    label comehere:
        menu:
            "She said “wow i will help anyone who knew my father! I think i got something, my dad used to always sit  thinking underneath the avocado tree “ look underneath the tree the key must be there ":
                jump option6
            "She said “ oscar our dog died after my dad’s death he was really special to him “ look in the dog cage  -the key must be there ":
                jump option6
            "She said when he is home he used to usually sit on this green sofa “-the sofa has 3 pockets ":
                g-"Looked over the sofa and checked the pockets nothing is there except his very old cigars , I think you should re-pick the clue :"
                jump comehere

        label option6:
            "Perfect! We got the key and found it : what next Gustavo?Ok.so because the museum has a really tough security Pablo Ascobar took advantage of it. He knew that no one would think that the money was there  , so he decided to hide his money in one of the safes at the museum in Cartagena.go find out about it"
    g-"how should you enter the musem ?"
    menu:
        "try to corrupt the guard - beat your ass and call the cops":
            "dakmckda"
        "Through the window of the toilet at night ":
            jump key1
        "Dress up as a statue and wait until the museum closes":
            g-"Nice be quiet and don't move --After 5 hours- Ok i think it's safe now i'm going to look for the safe"
            jump key1
    label key1:
    g-" Ok found it Gustavio! But it's so weird NO MONEY HERE . I found note that says:"
    menu:
        "I Love chipotle":
            jump chipotle
        "I owe martino 100 dollars for tacos":
            jump tacos
        " are you sure you are in the right place?":
            jump right

    label chipotle:
        menu :
            "Yes,lets do it ":
                g-" HOLY SHIT!! I remember how much pablo loved this place i really suggest you go there I have a feeling the money is buried there , hurry up and go there!!!"

            "No this is stuipd!":
                g-" No [name] nothing is stuipd the note whatwever it was will give us some clue to find the money please be patient  "
                jump chipotle

            "I don’t understand what does it say ":
                g-"read it again carefully"
                jump key1
    label tacos:
        g-"Pablo always pays his debts, its weird - we have to go there Martino is our chef and a very good friend in chipotle. I feel we need to find him. there is only one chipotle place in the area so go there."
        menu:
            "Good let's eat there. I'm starving":
                g- "Focus man. What are you doin? Just go there already, if you find the money there will be the billionars of this century for the rest of our lives"

            "I feel we should not go there WTF chipotle is a restaurent how will it have this amount of money  maybe we took a wrong decision , i'll go back to the pablo yard to ask his daughter for more clues  ":
                jump  yard

    label right:
        menu:
            "i am gonna kill you Gustavio!. You are a liar ":
                jump gameOver
            "Is it a name code for something? ":
                g-" yes u right!!! Pablo used to say it every time we had a secret meeting. And we always made them at chipotle. Lets go quick we are close!"
                jump Tochipotle
            "Maybe we should try to look somewhere else in his house - come back to the key action.":
                jump yard
    label Tochipotle:
    g-"took you so long are you okay ?"
    g- "after 3 hours"
    g- " I can see from your location service you are there  "
    g- "now think where the money can be? , and act normal , Think good cause we won't have second chance, the people will be so suspicious and they might caught you looking for the money "
    menu:
        "There is a very suspicious loose protrusion here! ":
            " No its just a rat YOU STUIPID - someone is calling the police NOW "
            jump gameOver

        " Go to the kitchen maybe martino will know something":
            g-" yes martiono was a very good friend of pablo ,he will help us"
            "Ok im in the kitchen , martino is here he is such a kind man , im eating the best tacos now ,"
            g-"come on [name] try to get information about the money"
            " so after having one of the most amazing mexican meals ever , you asked him about pablo and he started talking about their memories together   "
            g- "I can give you the right now to tell him about the note you found beacuse i have a feeling he knows where the money is buried , so try to ask him indirectly "
            g- "he said something that  there a safe where pablo used to save his things(money)!! "
            g- "now here martino understood and got what you are saying he looked shocked like after all these years the day has came "
            martino- "amazing job kid , I'll let you know what i know at least i always trusted pablo and he always had a motto you know why at the time needed ,"
            martino-"so you told me you have they key and the note now im going to tell you something there is a safe in the wall behind gas in the kitchen i never opened it because i can't "
            martino-"pablo said that one day someone will come with the note this will be the key for opening the safe "
            martino-"here you are with a note "
            g-"what do you think the password"
            jump kitchen

        "It seems all normal, I think i'll check for another clue in the museum":
            jump key1
    label kitchen:
        menu:
            "chipotl100":
                "OMG OPENED YOU DID ITTTTT "
                jump win
            "escobar":
                "didn't work only have 1 try left"
                jump kitchen

            "taco100":
                " didn't work also "


    label win:
    "YOU WONN"

    return
