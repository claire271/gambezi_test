data = new ArrayBuffer(5)
dataView = new Uint8Array(data)
for(var i = 0;i < 5;i++) { dataView[i] = i; }

gambezi = new Gambezi("pivision.local:5809");
//gambezi.set_refresh_rate(1000);
gambezi.on_close = function() { console.log("RECONNECT"); };
gambezi.on_ready = function(event) {
	console.log(event);
}

offx = gambezi.get_node('pi_vision/v_batt');
//offx.set_double(10.5);
offx.on_update = function() {
	document.querySelector('#offx').value = Math.round(offx.get_float() * 100)/100;
	document.querySelector('#offy').value = Math.round(offy.get_double() * 100)/100;
}

offy = gambezi.get_node(['pi_ups', 'voltage_5v']);

gambezi.on_error = console.log;
