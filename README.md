# Zendesk Philips Hue Status

This is a basic script that will check the current number of tickets in a given Zendesk view. Based off the number of tickets in the queue, your light will be set to:

* `green`  if the ticket count is less than 10
* `yellow` if the ticket count is between 10 and 14
* `red` if the ticket is greater than 15

If you want to customize features for yourself, check out https://github.com/studioimaginaire/phue for how to interact with the phue library.

All recommendations are welcome on how to improve the script!
