import streamlit as st

# Sample content data (In a real app, this would come from APIs or databases)
content_data = {
    "Technology": [
        {"title": "AI in 2024: What to Expect", "url": "https://example.com/ai2024", "image_url": "https://example.com/ai_image.jpg"},
        {"title": "Top 10 Programming Languages", "url": "https://example.com/programming_languages", "image_url": "https://example.com/programming_image.jpg"},
    ],
    "Health": [
        {"title": "10 Tips for a Healthier Lifestyle", "url": "https://example.com/healthy_lifestyle", "image_url": "https://example.com/health_image.jpg"},
        {"title": "Mental Health Awareness", "url": "https://example.com/mental_health", "image_url": "https://example.com/mental_health_image.jpg"},
    ],
    "Entertainment": [
        {"title": "Top Movies to Watch in 2024", "url": "https://example.com/top_movies", "image_url": "https://example.com/movies_image.jpg"},
        {"title": "The Rise of Indie Music", "url": "https://example.com/indie_music", "image_url": "https://example.com/music_image.jpg"},
    ],
    "Finance": [
        {"title": "Best Investment Strategies for 2024", "url": "https://example.com/investment_strategies", "image_url": "https://example.com/finance_image.jpg"},
        {"title": "Understanding Cryptocurrency", "url": "https://example.com/cryptocurrency", "image_url": "https://example.com/crypto_image.jpg"},
    ]
}

# Streamlit UI
st.title("Content Curator")

# User Preferences
st.write("Select your content preferences:")
preferences = st.multiselect("Content Categories:", list(content_data.keys()))

if st.button("Show Curated Feed"):
    if preferences:
        st.write("### Your Curated Content Feed:")
        for category in preferences:
            st.write(f"#### {category}")
            for item in content_data[category]:
                st.image(item["image_url"], caption=item["title"], use_column_width=True)
                st.write(f"[Read more]({item['url']})")
                st.write("---")
    else:
        st.write("Please select at least one category to see your curated feed.")

