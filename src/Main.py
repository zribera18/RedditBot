__author__ = 'Zach'

import praw
from Tkinter import *
from pyowm import *
import warnings

warnings.filterwarnings("ignore")

def main():
    root = Tk()

    API_key = '997b1736be3247534d9c7fd6907248f0'
    owm = OWM(API_key)
    # registry = owm.city_id_registry()
    # registry.id_for("New York,US")        # Gives: 5128581
    # registry.location_for("New York,US")
    place = 'San Diego, Ca'
    obs = owm.weather_at_place(place)
    w = obs.get_weather()
    # print(w.get_sunrise_time())
    temp = w.get_temperature('fahrenheit')
    status = w.get_detailed_status()
    currentWeather = "Current temperature in " + place + " is " + str(temp.get('temp')) + ", with " + str(status) + "."
    # print("\n")
    # print(temp.get('temp'))
    # import pprint
    # pprint.pprint(temp)
    # print(temp)

    r = praw.Reddit(user_agent='news_reader; u/<REDACTED> version 0.0.1')
    submissionsNews = list(r.get_subreddit('news').get_hot(limit=10))
    submissionsUplifting = list(r.get_subreddit('upliftingnews').get_top_from_day(limit = 10))
    submission_form = "{}) {} <{}>"
    count = 1
    print("Top 30 Posts from /r/news & /r/upliftingnews")
    print('-' * 25)

    T = Text(root)
    T.pack(side=LEFT, fill=BOTH, expand=YES)

    # sub = submissions[0]
    for x in range(submissionsNews.__len__()):
        sub = submissionsUplifting[x]
        quote = (submission_form.format(count, sub.title, sub.url))
        T.insert(END, "\n" + quote)

        count += 1
        sub = submissionsNews[x]
        quote = (submission_form.format(count, sub.title, sub.url))
        T.insert(END, "\n" + quote)
        count += 1




    # textPad = ScrolledText(root, width=50, height=40)
    # textPad.pack()
    # root.mainloop()
    label = Label(root, text=currentWeather)
    # label.pack()
    root.mainloop()


main()





# def printName(event):
# print("my name is jonas")
#
# button_1 = Button(root, text="Print name")
# button_1.bind("<Button-1>", printName)
# button_1.pack()


# label_1 = Label(root, text="Name:")
# label_2 = Label(root, text="Passwurd:")
# entry_1 = Entry(root)
# entry_2 = Entry(root)
#
# label_1.grid(row=0, column=0, sticky=E)
# label_2.grid(row=1, column=0, sticky=E)
#
# entry_1.grid(row=0, column=1)
# entry_2.grid(row=1, column=1)
#
# checkbox = Checkbutton(root, text="Keep me logged in")
# checkbox.grid(columnspan=2)

# one = Label(root, text="One", bg="red", fg="white")
# one.pack()
#
# two = Label(root, text="Two", bg="green", fg="white")
# two.pack(fill=X)
#
# three = Label(root, text="Three", bg="blue", fg="white")
# three.pack(side=LEFT, fill=Y)


# topFrame = Frame(root)
# topFrame.pack()
# bottomFrame = Frame(root)
# bottomFrame.pack(side=BOTTOM)
#
# button1 = Button(topFrame, text="Button1", fg="blue", command=printName())
# button2 = Button(topFrame, text="Button2", fg="red")
# button3 = Button(topFrame, text="Button3", fg="green")
# button4 = Button(bottomFrame, text="Button4", fg="black")
#
# button1.pack(side=LEFT)
# button2.pack(side=LEFT)
# button3.pack(side=LEFT)
# button4.pack(side=BOTTOM)

# label = Label(root, text=currentWeather)
# label.pack()


# import praw
#
# user_agent = ("Karma breakdown 1.0 by /u/_Daimon_ "
#               "github.com/Damgaard/Reddit-Bots/")
# r = praw.Reddit(user_agent=user_agent)
# thing_limit = 10
# user_name = "<REDACTED>"
# user = r.get_redditor(user_name)
# gen = user.get_comments(limit=thing_limit)
# karma_by_subreddit = {}
# for thing in gen:
#     subreddit = thing.subreddit.display_name
#     karma_by_subreddit[subreddit] = (karma_by_subreddit.get(subreddit, 0)
#                                      + thing.score)
# import pprint
# pprint.pprint(karma_by_subreddit)
