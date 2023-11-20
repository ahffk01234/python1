package day05;

import java.awt.EventQueue;
import java.awt.TextArea;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JLabel;
import javax.swing.JTextField;
import javax.swing.JButton;
import javax.swing.JTextArea;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;
import java.awt.event.KeyAdapter;
import java.awt.event.KeyEvent;

public class MySwing04 extends JFrame {

	private JPanel contentPane;
	private JTextField tf;
	JTextArea ta;
	

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					MySwing04 frame = new MySwing04();
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
	public MySwing04() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 403, 495);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));

		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		JLabel lbl = new JLabel("단수");
		lbl.setBounds(114, 58, 53, 23);
		contentPane.add(lbl);
		
		tf = new JTextField();
		tf.setBounds(196, 58, 71, 23);
		contentPane.add(tf);
		tf.setColumns(10);
		
		ta = new JTextArea();
		ta.setBounds(101, 175, 174, 190);
		contentPane.add(ta);
		
		JButton btn = new JButton("출력하기");
		btn.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				myClick();
			}
		});
		btn.setBounds(137, 109, 97, 23);
		contentPane.add(btn);
		
	}
	
	public void myClick() {
		String dan = tf.getText();
		String str = "";
		
		for(int i = 1; i < 10;i++) {
			str += dan + " * " + i + " = " + (i*Integer.parseInt(dan)) + "\n";
		}
		
		ta.setText(str);
	}
}
