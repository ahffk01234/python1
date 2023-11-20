package day05;

import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JLabel;
import javax.swing.JCheckBox;
import javax.swing.JButton;
import javax.swing.AbstractAction;
import java.awt.event.ActionEvent;
import javax.swing.Action;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;

public class MySwing01 extends JFrame {

	private JPanel contentPane;
//	private final Action action = new SwingAction();

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					MySwing01 frame = new MySwing01();
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
	public MySwing01() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 450, 300);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));

		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		JLabel lbl = new JLabel("good morning");
		lbl.setBounds(141, 43, 109, 32);
		contentPane.add(lbl);
		
		JButton btn = new JButton("click");
		
		btn.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				System.out.println("myclick");
				lbl.setText("good Evening");
			}
		});
		btn.setBounds(266, 48, 97, 23);
		contentPane.add(btn);
		
		
	}
	
//	private class SwingAction extends AbstractAction {
//		public SwingAction() {
//			putValue(NAME, "SwingAction");
//			putValue(SHORT_DESCRIPTION, "Some short description");
//		}
//		public void actionPerformed(ActionEvent e) {
//		}
//	}
}
