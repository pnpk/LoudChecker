import slackweb
import settings

slack = slackweb.Slack(url=settings.SLACK_WEBHOOK_URL)
slack.notify(text="Pythonからslackへ通知する")
