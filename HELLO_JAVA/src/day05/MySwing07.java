package day05;

import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JOptionPane;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JTextField;
import javax.swing.JButton;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;
import javax.swing.SwingConstants;

public class MySwing07 extends JFrame {

	private JPanel contentPane;
	private JTextField tf;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					MySwing07 frame = new MySwing07();
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
	public MySwing07() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 304, 360);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));

		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		tf = new JTextField();
		tf.setHorizontalAlignment(SwingConstants.RIGHT);
		tf.setBounds(46, 30, 196, 21);
		contentPane.add(tf);
		tf.setColumns(10);
		
		JButton btn1 = new JButton("1");
		btn1.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				String text = btn1.getText();
				addText(text);
			}
		});
		btn1.setBounds(46, 90, 49, 30);
		contentPane.add(btn1);
		
		JButton btn2 = new JButton("2");
		btn2.addMouseListener(new MouseAdapter() {
			public void mouseClicked(MouseEvent e) { myclick(e); }
		});
		btn2.setBounds(120, 90, 49, 30);
		contentPane.add(btn2);
		
		JButton btn3 = new JButton("3");
		btn3.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				String text = btn3.getText();
				addText(text);
			}
		});
		btn3.setBounds(193, 90, 49, 30);
		contentPane.add(btn3);
		
		JButton btn4 = new JButton("4");
		btn4.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				String text = btn4.getText();
				addText(text);
			}
		});
		btn4.setBounds(46, 138, 49, 30);
		contentPane.add(btn4);
		
		JButton btn5 = new JButton("5");
		btn5.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				String text = btn5.getText();
				addText(text);
			}
		});
		btn5.setBounds(120, 138, 49, 30);
		contentPane.add(btn5);
		
		JButton btn6 = new JButton("6");
		btn6.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				String text = btn6.getText();
				addText(text);
			}
		});
		btn6.setBounds(193, 138, 49, 30);
		contentPane.add(btn6);
		
		JButton btn7 = new JButton("7");
		btn7.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				String text = btn7.getText();
				addText(text);
			}
		});
		btn7.setBounds(46, 189, 49, 30);
		contentPane.add(btn7);
		
		JButton btn8 = new JButton("8");
		btn8.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				String text = btn8.getText();
				addText(text);
			}
		});
		btn8.setBounds(120, 189, 49, 30);
		contentPane.add(btn8);
		
		JButton btn9 = new JButton("9");
		btn9.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				String text = btn9.getText();
				addText(text);
			}
		});
		btn9.setBounds(193, 189, 49, 30);
		contentPane.add(btn9);
		
		JButton btn0 = new JButton("0");
		btn0.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				String text = btn0.getText();
				addText(text);
			}
		});
		btn0.setBounds(46, 240, 49, 30);
		contentPane.add(btn0);
		
		JButton btnCall = new JButton("call");
		btnCall.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				alert();
			}
		});
		btn1.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				String text = btnCall.getText();
//				alert("Calling : ~");
			}
		});
		btnCall.setBounds(120, 240, 122, 30);
		contentPane.add(btnCall);
		
		JButton btnDel = new JButton("del");
		btnDel.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				String textfield = tf.getText();
				String str = "";
				
				char last = textfield.charAt(textfield.length()-1);
				System.out.println(last);
			}
		});
		btnDel.setBounds(182, 61, 60, 21);
		contentPane.add(btnDel);
	}

	protected void alert() {
		String message = "";
		message += "Calling : " + tf.getText();
		JOptionPane.showMessageDialog(null, message, "전화거는 중", JOptionPane.INFORMATION_MESSAGE);
		JOptionPane.showMessageDialog(this, message );
	}

	protected void addText(String text) {
		String field = tf.getText();
		tf.setText(field + text);
		if(field.length() == 3 ) {
			tf.setText(field+"-");
		}
		if(field.length() == 8 ) {
			tf.setText(field+"-");
		}
	}
	public  void myclick(MouseEvent e) {
		
		String str_old = tf.getText();
		
		JButton imsi = (JButton)e.getSource();
		String str_new = imsi.getText();
		
		tf.setText(str_old + str_new);
	}

}
