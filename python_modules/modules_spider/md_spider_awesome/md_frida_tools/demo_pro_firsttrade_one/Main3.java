import javax.crypto.Cipher;
import javax.crypto.SecretKeyFactory;
import javax.crypto.spec.PBEKeySpec;
import javax.crypto.spec.PBEParameterSpec;
import java.security.spec.KeySpec;
import java.util.Arrays;

public class Main2 {
    public static void main(String[] args) throws Exception {
        // ����
        // Y,z,U,w,Z,W,I,y,M,T,c,t,O,W,Z,k,M,i,0,0,O,G,M,4,7,7,1,5,8,9,S
        char[] password = "YzUwZWIyMTctOWZkMi00OGM4771589S".toCharArray();
        // �Σ�16�����ַ���ת��Ϊ�ֽ����飩
        byte[] salt = new byte[]{(byte) 0xfa, (byte) 0x41, (byte) 0x5f, (byte) 0x14, (byte) 0xfd, (byte) 0xea, (byte) 0x9a, (byte) 0xc5};
        // ��������
        int iterationCount = 1000;
        // ��Կ����
        int keyLength = 64;

        // ����PBEKeySpec
        KeySpec keySpec = new PBEKeySpec(password, salt, iterationCount, keyLength);
        // ����SecretKeyFactory
        SecretKeyFactory keyFactory = SecretKeyFactory.getInstance("PBEwithMD5andDES");
        // ������Կ
        javax.crypto.SecretKey secretKey = keyFactory.generateSecret(keySpec);

        // ����PBEParameterSpec
        PBEParameterSpec parameterSpec = new PBEParameterSpec(salt, iterationCount);

        // ����Cipherʵ������ʼ��Ϊ����ģʽ
        Cipher cipher = Cipher.getInstance("PBEwithMD5andDES");
        cipher.init(Cipher.DECRYPT_MODE, secretKey, parameterSpec);

        // ���ܺ������
        byte[] encryptedData = new byte[]{(byte) 51, (byte) 53, (byte) 61, (byte) 83, (byte) 85, (byte) 48, (byte) 55, (byte) 1, (byte) 21, (byte) 5, (byte) 45, (byte) 50, (byte) 49, (byte) 52, (byte) 55, (byte) 52, (byte) 56, (byte) 51, (byte) 54, (byte) 52, (byte) 56, (byte) 18, (byte) 57, (byte) 54, (byte) 49, (byte) 51, (byte) 94, (byte) 56, (byte) 4, (byte) 53, (byte) 50, (byte) 55, (byte) 54, (byte) 94, (byte) 83, (byte) 69, (byte) 72, (byte) 75, (byte) 4, (byte) 55, (byte) 48, (byte) 55, (byte) 54, (byte) 94, (byte) 78, (byte) 65, (byte) 83, (byte) 68, (byte) 4, (byte) 57, (byte) 54, (byte) 49, (byte) 55, (byte) 94, (byte) 48, (byte) 54, (byte) 47, (byte) 48, (byte) 51, (byte) 47, (byte) 50, (byte) 48, (byte) 50, (byte) 52, (byte) 32, (byte) 48, (byte) 48, (byte) 58, (byte) 48, (byte) 48, (byte) 58, (byte) 48, (byte) 48, (byte) 48, (byte) 4, (byte) 53, (byte) 55, (byte) 52, (byte) 94, (byte) 48, (byte) 51, (byte) 4, (byte) 21, (byte) 17};

        // ȷ���������ݳ�����8�ı���
        if (encryptedData.length % 8 != 0) {
            throw new IllegalArgumentException("===Encrypted data length is not a multiple of 8===");
        }

        // ��������
        byte[] decryptedData = cipher.doFinal(encryptedData);

        // ��ӡ���ܽ��
        System.out.println("Decrypted Data: " + Arrays.toString(decryptedData));
        System.out.println("Decrypted String: " + new String(decryptedData));
    }
}

// ����java����: https://www.bejson.com/runcode/java/
// ����java����ִ��������:
// Decrypted Data: [71, 114, 56, 57, 76, 77]
// Decrypted String: Gr89LM

