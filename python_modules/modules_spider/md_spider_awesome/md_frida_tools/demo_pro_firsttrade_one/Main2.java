import javax.crypto.Cipher;
import javax.crypto.SecretKeyFactory;
import javax.crypto.spec.PBEKeySpec;
import javax.crypto.spec.PBEParameterSpec;
import java.security.spec.KeySpec;
import java.util.Arrays;

public class Main2 {
    public static void main(String[] args) throws Exception {
        // 密码
        //char[] password = "771589S".toCharArray();
        // Y,z,U,w,Z,W,I,y,M,T,c,t,O,W,Z,k,M,i,0,0,O,G,M,4,7,7,1,5,8,9,S
        char[] password = "YzUwZWIyMTctOWZkMi00OGM4771589S".toCharArray();
        // 盐（16进制字符串转换为字节数组）
        // byte[] salt = new byte[]{(byte) 0x2a, (byte) 0xe3, (byte) 0x01, (byte) 0xee, (byte) 0x68, (byte) 0x6c, (byte) 0x69, (byte) 0x15};
        // 8dcb9d28dc7954bb
        byte[] salt = new byte[]{(byte) 0x8d, (byte) 0xcb, (byte) 0x9d, (byte) 0x28, (byte) 0xdc, (byte) 0x79, (byte) 0x54, (byte) 0xbb};
        // 迭代次数
        int iterationCount = 1000;
        // 密钥长度
        int keyLength = 64;

        // 创建PBEKeySpec
        KeySpec keySpec = new PBEKeySpec(password, salt, iterationCount, keyLength);
        // 创建SecretKeyFactory
        SecretKeyFactory keyFactory = SecretKeyFactory.getInstance("PBEwithMD5andDES");
        // 生成密钥
        javax.crypto.SecretKey secretKey = keyFactory.generateSecret(keySpec);

        // 创建PBEParameterSpec
        PBEParameterSpec parameterSpec = new PBEParameterSpec(salt, iterationCount);

        // 创建Cipher实例并初始化为解密模式
        Cipher cipher = Cipher.getInstance("PBEwithMD5andDES");
        cipher.init(Cipher.DECRYPT_MODE, secretKey, parameterSpec);

        // 加密后的数据
        // byte[] encryptedData = new byte[]{(byte) -13, (byte) -27, (byte) 93, (byte) 93, (byte) 24, (byte) -55, (byte) 81, (byte) -76};
        // 64,-32,-81,-120,110,80,-68,123,-61,44,-120,-97,72,-54,-73,14,-25,108,-90,38,58,75,-49,-25,124,-112,-35,20,-113,-18,-127,78,-49,35,-21,62,45,99,58,-83,-20,55,18,-128,42,120,-43,0,-59,-95,-26,32,27,-33,-98,65,103,-37,-116,41,-107,78,-15,48,47,100,-23,32,47,93,-92,106,-70,16,-72,91,123,123,47,55,28,-7,-122,88,-3,-92,46,-94,24,-79,-110,107,-124,72,-10,-118,-113,-50,36,-119,-87,87,-119,-109,-114,-61,-2,25,71,117,-48,29,-115,-49,91,-50,66,-31,43,-9,-1,-64,120,-54,57,-112,125,-21,28,-67,-96,-24,43,97,65,115,-10,127,-92,-63,12,47,-74,-54,54,33,-101,-9,-71,91,109,-89,-19,-5,100,89,50,-44,-119,-11,67,126,-4,-34,-45,0,-57,9,-16,-115,104,-13,-75,-104,-12,-67,18,-50,68,-118,100,-118,89,-4,-7,-41,76,-108,-126,88,-29,-113
        byte[] encryptedData = new byte[]{(byte) 64, (byte) -32, (byte) -81, (byte) -120, (byte) 110, (byte) 80, (byte) -68, (byte) 123, (byte) -61, (byte) 44, (byte) -120, (byte) -97, (byte) 72, (byte) -54, (byte) -73, (byte) 14, (byte) -25, (byte) 108, (byte) -90, (byte) 38, (byte) 58, (byte) 75, (byte) -49, (byte) -25, (byte) 124, (byte) -112, (byte) -35, (byte) 20, (byte) -113, (byte) -18, (byte) -127, (byte) 78, (byte) -49, (byte) 35, (byte) -21, (byte) 62, (byte) 45, (byte) 99, (byte) 58, (byte) -83, (byte) -20, (byte) 55, (byte) 18, (byte) -128, (byte) 42, (byte) 120, (byte) -43, (byte) 0, (byte) -59, (byte) -95, (byte) -26, (byte) 32, (byte) 27, (byte) -33, (byte) -98, (byte) 65, (byte) 103, (byte) -37, (byte) -116, (byte) 41, (byte) -107, (byte) 78, (byte) -15, (byte) 48, (byte) 47, (byte) 100, (byte) -23, (byte) 32, (byte) 47, (byte) 93, (byte) -92, (byte) 106, (byte) -70, (byte) 16, (byte) -72, (byte) 91, (byte) 123, (byte) 123, (byte) 47, (byte) 55, (byte) 28, (byte) -7, (byte) -122, (byte) 88, (byte) -3, (byte) -92, (byte) 46, (byte) -94, (byte) 24, (byte) -79, (byte) -110, (byte) 107, (byte) -124, (byte) 72, (byte) -10, (byte) -118, (byte) -113, (byte) -50, (byte) 36, (byte) -119, (byte) -87, (byte) 87, (byte) -119, (byte) -109, (byte) -114, (byte) -61, (byte) -2, (byte) 25, (byte) 71, (byte) 117, (byte) -48, (byte) 29, (byte) -115, (byte) -49, (byte) 91, (byte) -50, (byte) 66, (byte) -31, (byte) 43, (byte) -9, (byte) -1, (byte) -64, (byte) 120, (byte) -54, (byte) 57, (byte) -112, (byte) 125, (byte) -21, (byte) 28, (byte) -67, (byte) -96, (byte) -24, (byte) 43, (byte) 97, (byte) 65, (byte) 115, (byte) -10, (byte) 127, (byte) -92, (byte) -63, (byte) 12, (byte) 47, (byte) -74, (byte) -54, (byte) 54, (byte) 33, (byte) -101, (byte) -9, (byte) -71, (byte) 91, (byte) 109, (byte) -89, (byte) -19, (byte) -5, (byte) 100, (byte) 89, (byte) 50, (byte) -44, (byte) -119, (byte) -11, (byte) 67, (byte) 126, (byte) -4, (byte) -34, (byte) -45, (byte) 0, (byte) -57, (byte) 9, (byte) -16, (byte) -115, (byte) 104, (byte) -13, (byte) -75, (byte) -104, (byte) -12, (byte) -67, (byte) 18, (byte) -50, (byte) 68, (byte) -118, (byte) 100, (byte) -118, (byte) 89, (byte) -4, (byte) -7, (byte) -41, (byte) 76, (byte) -108, (byte) -126, (byte) 88, (byte) -29, (byte) -113};

        // 解密数据
        byte[] decryptedData = cipher.doFinal(encryptedData);

        // 打印解密结果
        System.out.println("Decrypted Data: " + Arrays.toString(decryptedData));
        System.out.println("Decrypted String: " + new String(decryptedData));
    }
}

// 在线java环境: https://www.bejson.com/runcode/java/
// 在线java环境执行输出结果:
// Decrypted Data: [71, 114, 56, 57, 76, 77]
// Decrypted String: Gr89LM

