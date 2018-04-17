entity_night_light = "light.wohnzimmerfarblicht"
old_states = hass.states.get(entity_colorlight)
old_state = old_states.state
for x in range(0, 10):
    hass.services.call('light', 'turn_on', { "entity_id" : entity_colorlight, "color_name":"red"})
    time.sleep(0.5)
    hass.services.call('light', 'turn_on', { "entity_id" : entity_colorlight, "color_name":"blue"})
    time.sleep(0.5)
hass.services.call('light', 'turn_on', 
    { "entity_id" : entity_colorlight,
    "brightness": old_state.attributes["brightness"],
    "rgb_color":old_state.attributes["rgb_color"]})
logger.info("alarm flash done")
