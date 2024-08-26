import streamlit as st
import requests

st.title("Restraunt Recommendation System")

dish_names=st.text_input("Enter dish names:" )
print(dish_names)

if st.button("Recommend"):
    if dish_names=="":
        st.warning("Please enter at least one dish")
    else:
        try:
            dish_names_list=dish_names.split(",")
            query_string=""
            for dish in dish_names_list:
                dish=dish.strip()
                if query_string:
                    query_string+="&"
                query_string += f"dish_names={dish}"

            response=requests.get(f"http://localhost:8000/?{query_string}")
            if response.status_code==200:
                recommended_restaraunts=response.json().get("recommended restraunts",[])
                if recommended_restaraunts:
                    st.header("Recommended Restraunts")
                    for restraunt in recommended_restaraunts:
                        name=restraunt['name'].capitalize()
                        rating=restraunt['rating']
                        with st.container(height=100, border=True):
                            st.write(f":green[Name] - :blue{name}")
                            st.write(f":green[Rating]- :blue{rating}")

                else:
                    st.warning("restraunts not found")
            else:
                st.error("failed to fetch recommended restraunt, try again later")
        except Exception as e:
            st.error(f"oh we have some error{str(e)} ")

    