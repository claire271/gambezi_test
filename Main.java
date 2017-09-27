import com.tigerhuang.gambezi.*;
import com.tigerhuang.gambezi_dashboard.*;

public class Main implements OnReadyListener, OnUpdateListener {
	public static void main(String[] args) {
		new Main();
	}

	public Main() {
		System.out.println("Hello World");
		Gambezi gambezi = new Gambezi("localhost:7709", true, 5);
		gambezi.set_refresh_rate(10);
		gambezi.on_ready = this;

		Node a = gambezi.register_key(new String[]{"a"});
		a.update_subscription(100);
		a.on_update = this;

		while(true) {
			try {
				Thread.sleep(1000);
			}
			catch (InterruptedException  ex) {
				ex.printStackTrace();
			}
			System.out.print(".");
			gambezi.register_key(new String[]{"camera", "offx"}).set_float(12.6f);
			//GambeziDashboard.set_float("camera/offx", 12.6f);
		}
	}

	public void on_ready() {
		System.out.println("CONNECTED!!!");
	}

	public void on_update(Node node) {
		System.out.println(node.get_float());
	}
}
