data = new ArrayBuffer(5)
dataView = new Uint8Array(data)
for(var i = 0;i < 5;i++) { dataView[i] = i; }

gambezi = new Gambezi("localhost:7709", true);
//gambezi.set_refresh_rate(1000);
gambezi.on_close = function() { console.log("RECONNECT"); };

gambezi.set_refresh_rate(100);

offx = gambezi.register_key(['camera', 'offx']);
offx.update_subscription(1);
offx.on_update = function() {
	//console.log(offx.get_float() + ", " + offy.get_float());
	document.querySelector('#offx').value = offx.get_float();
	document.querySelector('#offy').value = offy.get_float();
}

offy = gambezi.register_key(['camera', 'offy']);
offy.update_subscription(1);

gambezi.on_error = console.log;
