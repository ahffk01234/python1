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

public class MySwing08 extends JFrame {

	private JPanel contentPane;
	private JTextField tf;
	private JTextArea ta;
	private int com;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					
					MySwing08 frame = new MySwing08();
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
	public MySwing08() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 281, 423);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));

		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		JLabel lbl = new JLabel("맞출수");
		lbl.setBounds(52, 52, 57, 15);
		contentPane.add(lbl);
		
		tf = new JTextField();
		tf.setBounds(121, 48, 85, 23);
		contentPane.add(tf);
		tf.setColumns(10);
		
		JButton btn = new JButton("맞춰보기");
		btn.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				guessNum();
			}
		});
		btn.setBounds(74, 92, 97, 23);
		contentPane.add(btn);
		
		ta = new JTextArea();
		ta.setBounds(52, 139, 151, 206);
		contentPane.add(ta);
		com = (int)(Math.random()*99)+1;
		System.out.println(com);
	}

	protected void guessNum() {
		
		String text = tf.getText();
		String ta_old = ta.getText();
		int myNum = Integer.parseInt(text);
		if(myNum > com) {
			ta.setText(ta_old + text + " DOWN\n");
		}
		else if(myNum < com) {
			ta.setText(ta_old + text + " UP\n");
			
		}else {
			JOptionPane.showMessageDialog(this, "성공");
			System.out.println("정답 : " + com);
		}
		tf.setText("");
	}
}
