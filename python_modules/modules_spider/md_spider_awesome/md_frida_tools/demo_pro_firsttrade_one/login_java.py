"""
 public final boolean e(String paramString1, String paramString2, String paramString3, String paramString4, int paramInt, String paramString5)
 {
     boolean bool2 = j.y(paramString1);
     boolean bool1 = true;
     if((!bool2) && (!j.y(paramString2)))
     {
         android.support.v4.media.f.z("c", "sendLogin", new Object[0]);
         this.B = 30;
         if((j.y(this.s)) || (j.y(this.t)) || (this.z != 1))
         {
             h();
         }
         this.x = paramInt;
         if(this.k != null)
         {
             this.k = null;
         }
         Object localObject = new o5.e(this.B, true);
         this.k = ((o5.e) localObject);
         ((o5.e) localObject).a = this;
         this.q = paramString1;
         this.r = paramString1;
         this.p = g5.b.i();
         try
         {
             paramString1 = KeyGenerator.getInstance("DESede").generateKey();
         }
         catch(NoSuchAlgorithmException paramString1)
         {
             paramString1.printStackTrace();
             paramString1 = null;
         }
         this.v = paramString1;
         ArrayList localArrayList = new ArrayList();
         localObject = Locale.US;
         localArrayList.add(String.format((Locale) localObject, "channel=%s", new Object[]
         {
             k(this.n)
         }));
         localArrayList.add(String.format((Locale) localObject, "country=%s", new Object[]
         {
             l(this.m)
         }));
         localArrayList.add(String.format((Locale) localObject, "lang=%s", new Object[]
         {
             m(this.o)
         }));
         localArrayList.add(String.format((Locale) localObject, "lid=%s", new Object[]
         {
             this.q
         }));
         localArrayList.add(String.format((Locale) localObject, "pwd=%s", new Object[]
         {
             paramString2
         }));
         if(!j.y(paramString4))
         {
             localArrayList.add(String.format((Locale) localObject, "fsec=%s", new Object[]
             {
                 g5.b.I(paramString4)
             }));
         }
         if(!j.y(paramString3))
         {
             localArrayList.add(String.format((Locale) localObject, "otp=%s", new Object[]
             {
                 paramString3
             }));
             if(this.m == 3)
             {
                 localArrayList.add(String.format((Locale) localObject, "keep_otp_flg=%s", new Object[]
                 {
                     paramString5
                 }));
             }
         }
         localArrayList.add(String.format((Locale) localObject, "key=%s", new Object[]
         {
             i.f(this.v.getEncoded())
         }));
         localArrayList.add(String.format((Locale) localObject, "ip=%s", new Object[]
         {
             this.p
         }));
         StringBuilder localStringBuilder = new StringBuilder();
         if(j.y(this.d))
         {
             paramString1 = "AppXXX";
         }
         else
         {
             paramString1 = this.d;
         }
         if(j.y(this.e))
         {
             paramString2 = "x.x.x(x)";
         }
         else
         {
             paramString2 = this.e;
         }
         if(j.y(this.f))
         {
             paramString3 = "x.x";
         }
         else
         {
             paramString3 = this.f;
         }
         if(j.y(this.g))
         {
             paramString4 = "UnknownBrand";
         }
         else
         {
             paramString4 = this.g;
         }
         paramInt = this.h;
         if((paramInt != -2147483648) && (paramInt > 0))
         {
             paramInt = this.i;
             if((paramInt != -2147483648) && (paramInt > 0) && (!Double.isNaN(this.j)) && (this.j > 0.0 D))
             {
                 paramString5 = String.format((Locale) localObject, "%dx%d_%.1fin", new Object[]
                 {
                     Integer.valueOf(this.h), Integer.valueOf(this.i), Double.valueOf(this.j)
                 });
                 break label665;
             }
         }
         paramString5 = "UnknownSize";
         label665: localStringBuilder.append(String.format((Locale) localObject, "%s_%s", new Object[]
         {
             paramString1, paramString2
         }));
         localStringBuilder.append(String.format((Locale) localObject, "|A%s", new Object[]
         {
             paramString3
         }));
         localStringBuilder.append(String.format((Locale) localObject, "|%s", new Object[]
         {
             paramString5
         }));
         localStringBuilder.append(String.format((Locale) localObject, "|%s", new Object[]
         {
             paramString4
         }));
         paramString1 = new StringBuilder();
         paramString1.append("AppVersionString[");
         paramString1.append(localStringBuilder.toString());
         paramString1.append("]");
         android.support.v4.media.f.l("c", paramString1.toString(), new Object[0]);
         localArrayList.add(String.format((Locale) localObject, "remark=%s", new Object[]
         {
             localStringBuilder.toString()
         }));
         paramString2 = g5.b.e("&", localArrayList);
         paramString3 = android.support.v4.media.f.n(this.u);
         if(paramString3 != null)
         {
             try
             {
                 paramString1 = new java / security / spec / X509EncodedKeySpec;
                 paramString1. < init > (paramString3);
                 paramString1 = KeyFactory.getInstance("RSA").generatePublic(paramString1);
             }
             catch(InvalidKeySpecException paramString1)
             {}
             catch(NoSuchAlgorithmException paramString1)
             {}
             paramString1.printStackTrace();
         }
         else
         {
             paramString1 = null;
         }
         if((paramString2 != null) && (paramString2.length() > 0) && (paramString1 != null))
         {
             paramString2 = g5.b.u(paramString2);
             if(paramString2 != null)
             {
                 try
                 {
                     paramString3 = Cipher.getInstance("RSA/ECB/PKCS1Padding");
                     paramString3.init(1, paramString1);
                     paramString1 = paramString3.doFinal(paramString2);
                 }
                 catch(Exception paramString1)
                 {
                     paramString1.printStackTrace();
                 }
             }
         }
         paramString1 = null;
         paramString1 = g5.b.I(android.support.v4.media.f.q(paramString1));
         paramString2 = String.format(Locale.US, "re=1&clm=%s", new Object[]
         {
             paramString1
         });
         android.support.v4.media.f.l("c", "LoginG2 - %s [%s]", new Object[]
         {
             this.J, paramString2
         });
         if(!j.y(paramString1))
         {
             long l1 = this.k.d(1, 0, this.J, paramString2);
             if(l1 != -9223372036854775808 L)
             {
                 d(l1, this.x, 2, f1.d.n);
                 this.z = 3;
                 break label1061;
             }
         }
         else
         {
             android.support.v4.media.f.z("c", "SecKeyRef AddPublicKey Fail", new Object[0]);
         }
     }
     bool1 = false;
     label1061: return bool1;
 }
"""