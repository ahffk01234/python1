package day03;

public class Animal {
	int cnt_hair = 1000;
	
	public void tsshampoo() {
		cnt_hair += 100;
	}
	
	public static void main(String[] args) {
		Animal ani = new Animal();
		
		System.out.println("b:"+ani.cnt_hair);
		ani.tsshampoo();
		
		System.out.println("b:"+ani.cnt_hair);
	}
}
