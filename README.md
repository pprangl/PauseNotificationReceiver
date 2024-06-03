# PauseNotificationReceiver

You can use a custom action script which is 'blackholing' the events during a maintenance. The receiver will be set to 'no receiver' in the specific notification rule.
This is working with a notification rule on the top ('Please select Continue Checking Rules')

![CVP Custom Notification Rule with no receiver](/images/NotificationRule.png)

This script can be imported as a CVP action. 
There are three arguments required:

| Name     | Type    | Required |
| -------- | ------- | -------- |
| DeviceID | Dynamic | Yes      |
| state    | Static  | Yes      | 
| token    | Static  | Yes      | 

Under the token you have to paste a service account token. 

Now you can assign the action to your CC template (so all devices involved get tagged) because of the state of 'yes'.

After the maint you would have the same action with the state of 'no'. This would remove the main tag from the devices again. 
