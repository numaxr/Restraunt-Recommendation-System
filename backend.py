from fastapi import FastApi, Query
from typing import List
import json

app=FastApi()

with open("restraunts.json","r") as file:
    data=json.load(file)


@app.get("/")
def get_restraunts(dish_names:List[str]=Query(...)):
    dish_names=[dish.lower() for dish in dish_names]
    restraunts=recommendRestraunts(dish_names)
    return {"recommended restraunts":restraunts}


def recommendRestraunts(dish_names):

    filtered_restraunts=filter(
        lambda restraunt: all (dish in restraunt.get("dishes",[]) for dish in dish_names), data)
    
    filtered_restraunts=list(filtered_restraunts)

    sorted_restraunts=sorted(filtered_restraunts, key=lambda x: x['rating'], reverse=True)

    return sorted_restraunts


