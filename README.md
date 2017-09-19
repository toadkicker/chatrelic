# Chatrelic

Have your Amazon Alexa device manage your New Relic alerts.

## Requirements

- Amazon Web Services Lambda
- Amazon Developer portal account
- New Relic account with alerts configured

## Features

- Receives an alert via New Relic alerts API and pushes to Alexa
- Allows user to ask Alexa for open alerts
  - "Alexa, ask Chatrelic if I have any new incidents."

## Setup

**AWS N. Virginia (US-East-1) is required for this to work correctly**

I don't make the rules, I just follow them.

* Open handler.py and add your New Relic API key. Refer to
[the docs](https://docs.newrelic.com/docs/alerts/rest-api-alerts/new-relic-alerts-rest-api) for obtaining your key.
* Create a zip file with the repo contents.
* Create a Lambda in AWS Console or use the CLI:

```
aws lambda create-function --function-name chatrelic --runtime python3.6 --code repo.zip
```

Take note of the ARN of the new function (`arn:aws:lambda:us-east-1:1234567890:function:chatrelic`)

Once installed head over to the Alexa [developer portal](https://developer.amazon.com).

* Create a new skill
  * Name it anything, like `Chatrelic` for example
  * For the invocation, this is what you will want to say to Alexa to
  invoke the skill.
* Open skill_builder.json and paste it into the 'Code' section of the
interaction model builder.
  * Save the interaction model!
* Open Configuration and paste in the ARN of the lambda created above.

Test your chatrelic in the Alexa app, as developers automatically have
skills pushed to their own accounts.

## Contributing

There is a lot of ways this type of thing could go, so I welcome ideas
and contributions. Check out the issues tab if you want some ideas.


## Special Thanks

I would like to thank New Relic for generously donating an account while
I was developing this functionality.