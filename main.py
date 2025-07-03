from demographic_data_analyzer import demographic_data_analyzer

if _name_ == "_main_":
    result = demographic_data_analyzer()

    print("Race count:\n", result['race_count'], "\n")
    print("Average age of men:", result['average_age_men'])
    print("Percentage with Bachelors degrees:", result['percentage_bachelors'], "%")
    print("Percentage with higher education that earn >50K:", result['higher_education_rich'], "%")
    print("Percentage without higher education that earn >50K:", result['lower_education_rich'], "%")
    print("Min work hours:", result['min_work_hours'])
    print("Percentage of rich among those who work fewest hours:", result['rich_percentage'], "%")
    print("Country with highest percentage of rich:", result['highest_earning_country'])
    print("Highest percentage of rich people in country:", result['highest_earning_country_percentage'], "%")
    print("Top occupation in India for those who earn >50K:", result['top_IN_occupation'])
