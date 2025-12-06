from nemoguardrails import RailsConfig, LLMRails

#load library configration
config = RailsConfig.from_path("./config")
rails = LLMRails(config)

#chatbot loop
while(message := input(">")) != "end" : 
    response = rails.generate(messages=[{
        "role": "user",
        "content": message
    }])
    print(response["content"])