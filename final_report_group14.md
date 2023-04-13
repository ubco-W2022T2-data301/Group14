{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "b4bd5343-f948-405d-869d-3967810197c6",
   "metadata": {},
   "source": [
    "# **Group 14 Analysis on the Premier League Data from 2014-2020**"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "e9003d65-05ea-42d5-9c08-10883a3da6de",
   "metadata": {},
   "source": [
    "## **Team Members**\n",
    "- Takara Nishizaki\n",
    "- Omar Hemed\n",
    "- Makoto Kitamura"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "7d0e116c-6a8f-477c-885e-a9cadbb10939",
   "metadata": {
    "tags": []
   },
   "source": [
    "## **Introduction**"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "a70df43d-3b5d-4f46-ab76-288fd851e281",
   "metadata": {},
   "source": [
    "The Premier League is one of the most famous football leagues in the world, known for its high intensity and level of players. The three of us; Takara Nishizaki, Omar Hemed, and Makoto Kitamura analyzed the Premier League games between 2014-2020 (The original data can be accessed from [here](https://www.kaggle.com/datasets/sanjeetsinghnaik/premier-league-matches-20142020) ) from various perspectives, to see if there is a strong correlation between certain factors. The data from the Premier League was chosen because all three of us have an interest in football, and wanted to analyze statistical data that we are interested in while having some prior knowledge as well. Through the various categories and factors that are in the game of football, we came up with three research questions that can be answered to analyze the game further from a statistical viewpoint. "
   ]
  },
  {
   "cell_type": "markdown",
   "id": "e24371b6-9d34-412f-a117-bcef41b6e235",
   "metadata": {},
   "source": [
    "## **Research 1: Does playing at home affects the amount of yellow/red cards for the away team? (Omar Hemed)**"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "23351dab-4973-47d8-a0ca-b41ce48e0d2c",
   "metadata": {},
   "source": [
    "- The analysis notebook can be accessed from [here](https://github.com/ubco-W2022T2-data301/Group14/blob/main/analysis/analysis1.ipynb)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "1dade50b-c4b2-46e0-af3a-3b6bf774ca2e",
   "metadata": {},
   "source": [
    " The main focus of my research question was to gather as much data as I could for the yellow and red cards for the away team and compare them with the home team. I gathered the information for both yellow and red cards and calculated them per year, I also got the mean of all teams and the mean for yellow and red cards. After getting into more depth about my question I concluded that the away team gets more yellow/red cards for multiple reasons. One of the reasons is that the away team is not playing with its own fans and field and that affects the players and how well they can perform in a match. "
   ]
  },
  {
   "cell_type": "markdown",
   "id": "73cc81cf-1238-4ab9-9ce7-f2829c7142b6",
   "metadata": {},
   "source": [
    "![alt text](./images/\"Away Team Yellow Cards.png\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "73ec4550-c2ef-486f-b7d1-18cffadedf1d",
   "metadata": {},
   "source": [
    "![alt text](./images/\"Home Team Yellow Cards.png\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "cf67de38-b832-45d5-bf2a-b5a7c9c41800",
   "metadata": {},
   "source": [
    "I specifically chose to add the 2 graphs above to my dashboard since they are easy to read and convenient. As represented above we can see the number of yellow cards per year for both the home team and the away team. This is an easy visualization that can clearly show us the huge difference between the number of yellow cards the away team gets over the home team."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "dfbf7f22-a187-49ac-82ce-891294503ae1",
   "metadata": {},
   "source": [
    "![alt text](Group14/images/\"Away Team Red Cards.png\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "28479ea2-c1f5-498b-ac02-986285e54e7a",
   "metadata": {},
   "source": [
    "![alt text](./images/\"Home Team Red Cards.png\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "ab47fae5-befd-4923-8fa9-cf1dfbca982b",
   "metadata": {},
   "source": [
    "Moreover, I presented 2 graphs for red cards per year for both the home and the away team. It was a little bit harder to gather information about red cards since they are rare to happen. We can observe from these 2 graphs that still the away team gets more red cards than the home team over the years. And that concludes my research question that the away team gets more yellow and red cards than the home team for many different reasons."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "79dd9f64-4cfb-4d90-9bba-5c3b222b819a",
   "metadata": {},
   "source": [
    "## **Research 2:  How does the halftime score affect the result and excitement of the whole game? How does a score of the home game change the excitement of the fans and does having higher excitement affect even more goals for the home team? What other strong factors are contributing to the team winning the game? (Makoto Kitamura)**"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "7f8780f7-bf5b-4f6b-be94-bf8dcbe3fd69",
   "metadata": {},
   "source": [
    "- The analysis notebook can be accessed from [here](https://github.com/ubco-W2022T2-data301/Group14/blob/main/analysis/analysis2.ipynb)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "b2affddd-0d8b-4aa3-a01b-89596587ba69",
   "metadata": {},
   "source": [
    "My research was focused on exploring the impact of halftime scores and home game excitement on the overall result and excitement of a soccer match. Specifically, I was interested in understanding how a team’s halftime lead or deficit could affect their performance in the second half, and how the excitement of home fans could potentially influence the outcome of the game. While I found that these factors can have some impact, I also noted that there are many other factors that contribute to a team's success, such as player skill coaching tactics, and external factors like injuries or weather conditions. Overall my research highlights the complex and multifaceted nature of soccer as a sport and the many variables that can influence the outcome of a match."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "a54a065a-49ce-4eb2-94bd-fb57fc70d09d",
   "metadata": {},
   "source": [
    "![alt text](Group14/images/makoto.image1.png)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "0d4edc12-6cc3-4b80-8764-20b253f8a343",
   "metadata": {},
   "source": [
    "This graph reveals that matches with close scores, such as 0-0, 1-1, and 1-0 have the highest match excitement for the fans. This indicates that fans enjoy matches that are competitive and where the outcome is uncertain until the very end. It also suggests that a low-scoring match can be just as exciting, if not more so, than a high-scoring match."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "08435be0-3d15-4928-8d8c-20268b2bd157",
   "metadata": {},
   "source": [
    "![alt text](./images/makoto.image2.png)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "ef63d1fd-45b6-4521-a97c-ce8c03b14977",
   "metadata": {},
   "source": [
    "After analyzing the relationship between the final score and the match excitement, I found that the graph looks similar to the halftime score bs match excitement. Interestingly, this indicates that there was no clear correlation between the two graphs. This suggests that the level of match excitement at halftime may not necessarily be a good predictor of the final score.\n",
    "As you can see, even if the final score is high, there can be a decrease in overall match excitement in the latter stages of the game."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "1da44f4b-c36d-4442-9d2c-a4f8a4ce767c",
   "metadata": {},
   "source": [
    "![alt text](./images/makoto.image3.png)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "47b73d52-00a9-4c23-857c-fcefc7235e4b",
   "metadata": {},
   "source": [
    "I found from the last graph that there is a strong correlation between the possession ratio and the result score ratio. This suggests that the team with more possession tends to have a higher result score ratio. Result score ratio is calculated by dividing the home team’S result score by the awy team’s result score. Ratio inf(infinity) indicates that away team did not score any(divide by zero)."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "10d2ca31-959b-4ccc-acf9-7b04b8701012",
   "metadata": {},
   "source": [
    "From my analysis of the last graph, I found a strong correlation between possession ratio and result score ratio. This indicates that the team with more possession tends to have a higher result score ratio. Result score ratio is a metric I used to calculate the home team’s result score divided by the away team’s result score. If the away team did not score any goals, the ratio is undefined(indicated by infinity). \n",
    "This finding suggests that possession is an important factor indetermining the outcome of a match. Teams that are able to maintain possession of the ball for longer periods of time are more likely to create scoringopportunities and control the pace of the game. Additionally, possession can help to tire out the opposing team and limit their attacking opportunities."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "56a82106-2cb1-45bb-a2a1-cd86c27e53fd",
   "metadata": {},
   "source": [
    "## **Research 3:  How do cards affect the excitement of the fans watching the game in the stadium? Do more fouls lead to more cards? (Takara Nishizaki)**"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "ab41a822-9359-4464-838b-47e4e28dbc96",
   "metadata": {},
   "source": [
    "- The analysis notebook can be accessed from [here](https://github.com/ubco-W2022T2-data301/Group14/blob/main/analysis/analysis3.ipynb)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "25cf5aed-54f4-4c9a-a495-815d887dd191",
   "metadata": {},
   "source": [
    "For my research question, I wanted to focus on the relationship between the number of cards, and the rate of match excitement given out by the fans. I was curious about this because some people enjoy the game more when it gets heated with all of the aggressive and intense duals that are performed on the field. Therefore, I decided to make different tables that compare three categories from the dataset that we chose to work on. They are the Match Excitement, Fouls, and Yellow Cards categories. To conduct this, I wrangled the dataset into categories that are only necessary for my research, which are the Teams, Score, Match Excitement scale, and Yellow/Red cards. In addition to that, I have made three new columns that combine the sum of yellow/red cards and fouls, since those categories were separated into Home and Away. Finally, I made two new columns that categorize the number of fouls and yellow cards, so that it will be easier to see when I plot the graph later on in my research. "
   ]
  },
  {
   "cell_type": "markdown",
   "id": "93f1fd3b-47e2-4abd-b300-74838ec7105a",
   "metadata": {},
   "source": [
    "![alt text](./images/Takara_1.png)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "6c5e934f-dd55-49df-a475-8e3e8818cb76",
   "metadata": {},
   "source": [
    "First, I took the mean of yellow cards per year, using the groupby function. Here, we can see that the average number of yellow cards per game is approximately 3 to 4, and shows no significant change over the years. Usually, the league implements new rules and refereeing standards that change how the referees judge the game. However, we can see that it is not a significant factor that might affect the research."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "11adfa65-e373-4de4-8f75-9ca429d469c6",
   "metadata": {},
   "source": [
    "![alt text](./images/Takara_2.png)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "d49d66e9-05c8-473a-b087-79a589200e72",
   "metadata": {},
   "source": [
    "![alt text](./images/Takara_3.png)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "2a42868a-c747-4e84-90ce-cdbb47c0e45c",
   "metadata": {},
   "source": [
    "Next, I made two graphs that show the average number of cards that each team receives, and the number of fouls they commit when playing at home. The purpose of these two graphs was to see if more fouls committed will lead to more yellow cards given out as a penalty. When looking at the mean number of fouls, Watford has the highest number of fouls committed, while Liverpool has the second least number of fouls committed. With this information, looking at the mean number of yellow cards per team, Watford is also the highest in this category, and Liverpool is the team with the least cards given out. Therefore, we are able to see the correlation where more fouls lead to more yellow cards given out. The reason behind this is probably to keep the game away from getting too heated and to protect the players before getting into situations where they could get injured."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "b1cbda92-c25a-4dbb-9d5d-7085df80a3ae",
   "metadata": {},
   "source": [
    "![alt text](./images/Takara_4.png)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "7d281f7c-d38f-417a-ad64-2ba7cf237764",
   "metadata": {},
   "source": [
    "![alt_text](./images/Takara_5.png)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "b9b98b25-bfb2-4aa8-b322-b75dcdd7f539",
   "metadata": {},
   "source": [
    "Finally, to see the correlation between the match excitement and the number of fouls, I created a box plot along with a swarm plot. The box plot shows the relationship between the number of yellow cards and their match excitement. Here, it can be said that there is no significant evidence that more yellow cards will lead to fans being more excited. In fact, there are some outliers that show a high match excitement rate when having a few yellow cards. Next, the swarm plot shows the relationship between the number of fouls (which was categorized), and the match excitement rate. In the previous two graphs, there was a correlation between the number of yellow cards and fouls, so I decided to include this swarm plot. Here, it is similar to the previous box plot where no significant correlation was seen between the two, since the match excitement rate was spread out from 2-10, regardless of the number of fouls."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "35f6cd57-76fa-44a7-996b-0f63f8c61125",
   "metadata": {},
   "source": [
    "To conclude my individual research, I was not able to obtain significant evidence that the number of yellow cards increases the match excitement rate. The reason behind this may be that the fans want to watch their team win, regardless of how the team performs. In addition to that, each team has different playing styles that will make a difference in the number of fouls and yellow cards received. To answer the second part of the research question, more fouls do lead to more yellow cards, as shown by the previous graphs where there was a correlation between the two categories. Since football is a sport where a lot of different factors are involved, it was hard to say that one specific factor determines the match excitement rate. "
   ]
  },
  {
   "cell_type": "markdown",
   "id": "92866448-73aa-4542-9887-481158ee3af5",
   "metadata": {},
   "source": [
    "## **Conclusion**"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "23a7720a-a99f-4d5e-bb38-db415bfe55ff",
   "metadata": {},
   "source": [
    "It is interesting to see how some of the data show certain tendencies between categories, and how the playing style of the team can lead to different intensities, scores,  and penalization in the game. The biggest lesson from this research was that there are 22 players playing on the field at a time, while the coaches are making different decisions on the spot. With all of the different thoughts, perspectives, and emotions that can happen in the span of 90 minutes, it is hard to make a significant connection between data, as there are no guarantees in football. Yellow cards happen more often than red cards, and away teams can be more aggressive than the home team. Thre is a slight advantage for the home team because of the support from their fans. More fouls lead to more cards, as referees are trying to keep the game from getting out of hand. Finally, all of the analysis that was done during this project is a fact. However, the game of football is so much more than just a series of numbers and data. This research will definitely benefit to look at tendencies, but will not guarantee any results and outcome of the game, hence why people enjoy the game. "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "65f76919-1eb0-4fcb-a54b-70ec9c01d2b7",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
