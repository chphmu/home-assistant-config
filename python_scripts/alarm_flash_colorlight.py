entity_colorlight = "light.wohnzimmerfarblicht"
old_state = hass.states.get(entity_colorlight)
for x in range(0, 10):
    hass.services.call('light', 'turn_on', { "entity_id" : entity_colorlight, "color_name":"red"})
    time.sleep(0.5)
    hass.services.call('light', 'turn_on', { "entity_id" : entity_colorlight, "color_name":"blue"})
    time.sleep(0.5)
if (old_state.state == 'on'):
    hass.services.call('light', 'turn_on', 
        { "entity_id" : entity_colorlight,
        "brightness": old_state.attributes["brightness"],
        "rgb_color":old_state.attributes["rgb_color"]})
else:
    hass.services.call('light', 'turn_off', 
        { "entity_id" : entity_colorlight})
logger.info("alarm flash done")
