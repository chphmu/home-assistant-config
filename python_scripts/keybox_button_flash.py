for x in range(0, 10):
    hass.services.call('switch', 'turn_on', { "entity_id" : "switch.keybox_button1light"})
    hass.services.call('switch', 'turn_on', { "entity_id" : "switch.keybox_button2light"})
    hass.services.call('switch', 'turn_on', { "entity_id" : "switch.keybox_button3light"})
    hass.services.call('switch', 'turn_on', { "entity_id" : "switch.keybox_button4light"})
    hass.services.call('switch', 'turn_on', { "entity_id" : "switch.keybox_button5light"})
    time.sleep(0.5)
    hass.services.call('switch', 'turn_off', { "entity_id" : "switch.keybox_button1light"})
    hass.services.call('switch', 'turn_off', { "entity_id" : "switch.keybox_button2light"})
    hass.services.call('switch', 'turn_off', { "entity_id" : "switch.keybox_button3light"})
    hass.services.call('switch', 'turn_off', { "entity_id" : "switch.keybox_button4light"})
    hass.services.call('switch', 'turn_off', { "entity_id" : "switch.keybox_button5light"})
    time.sleep(0.5)
logger.info("keybox button flash done")
