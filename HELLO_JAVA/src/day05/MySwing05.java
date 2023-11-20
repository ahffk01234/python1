package day05;

import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JLabel;
import javax.swing.JButton;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;

public class MySwing05 extends JFrame {

	private JPanel contentPane;
	JLabel lbl1;
	JLabel lbl2;
	JLabel lbl3;
	JLabel lbl4;
	JLabel lbl5;
	JLabel lbl6;
	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					MySwing05 frame = new MySwing05();
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
	public MySwing05() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 450, 300);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));

		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		lbl1 = new JLabel("__");
		lbl1.setBounds(52, 49, 57, 15);
		contentPane.add(lbl1);
		
		lbl2 = new JLabel("__");
		lbl2.setBounds(109, 49, 57, 15);
		contentPane.add(lbl2);
		
		lbl3 = new JLabel("__");
		lbl3.setBounds(165, 49, 57, 15);
		contentPane.add(lbl3);
		
		lbl4 = new JLabel("__");
		lbl4.setBounds(221, 49, 57, 15);
		contentPane.add(lbl4);
		
		lbl5 = new JLabel("__");
		lbl5.setBounds(276, 49, 57, 15);
		contentPane.add(lbl5);
		
		lbl6 = new JLabel("__");
		lbl6.setBounds(334, 49, 57, 15);
		contentPane.add(lbl6);
		
		JButton btn = new JButton("로또 생성하기");
		btn.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				lotto();
			}
		});
		btn.setBounds(79, 105, 272, 23);
		contentPane.add(btn);
	}

	protected void lotto() {
		
		String[] lotto = new String[]{};
		
		for(int i = 0; i < 6; i++) {
			double rnd = Math.random()*46+1;
			String num = String.valueOf(Math.round(rnd));
			
			lotto[i] = num;
			
			if(i >1) {
				if(lotto[i].equals(lotto[i-1])) {
					i -= 1;
				}
				else {
					continue;
				}
			}
		}
		
		lbl1.setText(lotto[0]);
		lbl2.setText(lotto[1]);
		lbl3.setText(lotto[2]);
		lbl4.setText(lotto[3]);
		lbl5.setText(lotto[4]);
		lbl6.setText(lotto[5]);
	}

}
