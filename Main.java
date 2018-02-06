import com.tigerhuang.gambezi.OnUpdateListener;
import com.tigerhuang.gambezi.dashboard.GambeziDashboard;

public class Main {
	public static void main(String[] args) {
		new Main();
	}

	public Main() {
		System.out.println("Hello World");

		GambeziDashboard.get_boolean("test/double/in");
		GambeziDashboard.get_boolean("test/double/out");
		GambeziDashboard.get_boolean("test/string/in");
		GambeziDashboard.get_boolean("test/string/out");
		GambeziDashboard.get_boolean("test/boolean/in");
		GambeziDashboard.get_boolean("test/boolean/out");
		GambeziDashboard.get_boolean("test/button");

		GambeziDashboard.listen_button("test/button", new OnUpdateListener() {
			public void on_update(Object object) {
				GambeziDashboard.log_string("Button Pressed");
			}
		});

		int i = 0;
		while(true) {
			try {
				Thread.sleep(1000);
			}
			catch (InterruptedException  ex) {
				ex.printStackTrace();
			}
			System.out.println(".");
			System.out.println(GambeziDashboard.get_double("test/double/in"));
			System.out.println(GambeziDashboard.get_string("test/string/in"));
			System.out.println(GambeziDashboard.get_boolean("test/boolean/in"));

			GambeziDashboard.set_double("test/double/out", i);
			GambeziDashboard.set_string("test/string/out", ((i % 2) == 0) ? "Hi" : "Bye");
			GambeziDashboard.set_boolean("test/boolean/out", ((i % 2) == 0));
			GambeziDashboard.log_string("Index: " + i);

			i++;
		}
	}
}
