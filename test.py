import json
import handler

fixture = {
  "session": {
    "new": True,
    "sessionId": "SessionId.bc2ed2fb-05c9-47cd-afdc-37fb9cb1157a",
    "application": {
      "applicationId": "amzn1.ask.skill.ef7f8441-6d28-413c-ad21-1038fa32e012"
    },
    "attributes": {},
    "user": {
      "userId": "amzn1.ask.account.AGDVTVRBVEYAV2GMFSBBX5LKXHWMGJWHE7PSZGICHE4K2CXYVGSRUGLAWHOI3K7N7YHHW3GIZUCDY7JTOHKXVCVTKQXNJLAZ44EGWZAVL6GDUEPVETX43K3OYJ5U5JHQHUHEP3SSTUT5UV34HZ2O5JXMASFEIYUZJQRTTRAVLINNTXRQTIYIFF6CED4E6OX3E472K2TY7OE34JQ"
    }
  },
  "request": {
    "type": "IntentRequest",
    "requestId": "EdwRequestId.df541886-43a3-4207-8a96-cc9d783976e0",
    "intent": {
      "name": "events",
      "slots": {
        "AMAZON.DATE": {
          "name": "AMAZON.DATE"
        },
        "NEWRELIC_Alert": {
          "name": "NEWRELIC_Alert"
        }
      }
    },
    "locale": "en-US",
    "timestamp": "2017-09-06T05:52:56Z"
  },
  "context": {
    "AudioPlayer": {
      "playerActivity": "IDLE"
    },
    "System": {
      "application": {
        "applicationId": "amzn1.ask.skill.ef7f8441-6d28-413c-ad21-1038fa32e012"
      },
      "user": {
        "userId": "amzn1.ask.account.AGDVTVRBVEYAV2GMFSBBX5LKXHWMGJWHE7PSZGICHE4K2CXYVGSRUGLAWHOI3K7N7YHHW3GIZUCDY7JTOHKXVCVTKQXNJLAZ44EGWZAVL6GDUEPVETX43K3OYJ5U5JHQHUHEP3SSTUT5UV34HZ2O5JXMASFEIYUZJQRTTRAVLINNTXRQTIYIFF6CED4E6OX3E472K2TY7OE34JQ"
      },
      "device": {
        "supportedInterfaces": {}
      }
    }
  },
  "version": "1.0"
}

handler.lambda_handler(fixture, fixture["context"])