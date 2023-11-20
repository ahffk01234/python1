package day04;

import java.util.ArrayList;

public class Musk {
	ArrayList<String> companys = new ArrayList<String>();
	
	public void tell(String c_name) {
		companys.add(c_name);
	}

	public void show() {
		
		for(int i = 0; i < companys.size();i++) {
			System.out.println(companys.get(i));
		}
	}
}
