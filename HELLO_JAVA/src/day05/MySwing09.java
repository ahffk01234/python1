package day05;

import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JLabel;
import javax.swing.JOptionPane;
import javax.swing.JTextField;
import javax.swing.JButton;
import javax.swing.JTextArea;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;

public class MySwing09 extends JFrame {

	private JPanel contentPane;
	private JTextField tf;
	String com = "";
	private JTextArea ta;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					
					MySwing09 frame = new MySwing09();
					frame.setVisible(true);
				} catch (Exception e) {
					e.printStackTrace();
				}
			}
		});
	}

	/**
	 * Create the frame.
	 */
	public MySwing09() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 302, 382);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));

		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		JLabel lbl = new JLabel("스트라이크");
		lbl.setBounds(41, 35, 82, 15);
		contentPane.add(lbl);
		
		tf = new JTextField();
		tf.setBounds(135, 32, 103, 21);
		contentPane.add(tf);
		tf.setColumns(10);
		
		JButton btn = new JButton("맞춰보기");
		btn.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				myclick();
				
			}
		});
		btn.setBounds(51, 63, 180, 21);
		contentPane.add(btn);
		
		ta = new JTextArea();
		ta.setBounds(51, 106, 180, 198);
		contentPane.add(ta);
		ranC();
		
	}
	
	public void ranC() {
		int[] list = {0,1,2,3,4,5,6,7,8,9};
		for (int i = 0; i < 1000; i++) {
			
			int rnd = (int)(Math.random()*9)+1;
			
			int temp = list[0];
			list[0] = list[rnd];
			list[rnd] = temp;
		}
		com = list[0]+""+list[1]+""+list[2];
		System.out.println(com);
	}

	protected void myclick() {
		
		String mine = tf.getText();
		int s = getS(mine,com);
		int b = getB(mine,com);
		System.out.println("s " + s);
		String str_old = ta.getText();
		String str_new = mine +"-----" + s +"S"+b+"B\n";
		
		ta.setText(str_old + str_new);
		
		tf.setText("");
		if(s == 3) {
			JOptionPane.showMessageDialog(this, "축하합니다" + mine );
		}
		
	}

	protected int getB(String mine, String com) {
		
		int ret = 0;
		String m1 = mine.substring(0, 1);
		String m2 = mine.substring(1, 2);
		String m3 = mine.substring(2, 3);
		
		String c1 = com.substring(0, 1);
		String c2 = com.substring(1, 2);
		String c3 = com.substring(2, 3);
		
		if(m1.equals(c2) || m1.equals(c3)) ret++;
		if(m2.equals(c1) || m2.equals(c3)) ret++;
		if(m3.equals(c1) || m3.equals(c2)) ret++;
		
		return ret;
		
	}

	protected int getS(String mine, String com) {
		int ret = 0;
		String m1 = mine.substring(0, 1);
		String m2 = mine.substring(1, 2);
		String m3 = mine.substring(2, 3);
		
		String c1 = com.substring(0, 1);
		String c2 = com.substring(1, 2);
		String c3 = com.substring(2, 3);
		
		if(m1.equals(c1)) ret++;
		if(m2.equals(c2)) ret++;
		if(m3.equals(c3)) ret++;
		
		return ret;
	}

}
