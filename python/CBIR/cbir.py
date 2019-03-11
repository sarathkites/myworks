import tkinter as tk
from PIL import ImageTk, Image
import tkinter.ttk as ttk
#from tkinter import messagebox
import os #, sys
from tkinter.filedialog import askopenfilename
import shutil
import time
import cv2
import _pickle
#import numpy as np
from matplotlib import pyplot as plt 

LARGE_FONT= ("Verdana", 12)

DBASE="./dbase"
ALGO="./algo"
TEMP="./temp"
ALGOS = ('SIFT','ORB')

class CBIRUI(tk.Tk):

    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand = True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, PageTest, PageTrain,PageAdd,PageSearch):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()

        
class StartPage(tk.Frame):
    @staticmethod
    def featurenotactive():
          tk.messagebox.showinfo("Feature", "Feature not Enabled!!!!")

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)

        file = 'CBIR_web.png'
        px = 10
        py = 10
        fnt = "Verdana 14 bold"

        logo = ImageTk.PhotoImage(Image.open(file))
        w1 = tk.Label(self, image=logo,compound = tk.CENTER)
        w1.image = logo
        w1.pack(pady=10,padx=10)
        
        add_bt = tk.Button(self, 
              compound=tk.CENTER,
              padx = px,
              pady=py, 
              font = fnt,
              command=lambda: controller.show_frame(PageAdd),
              text='Add').pack(side="left")
        train_bt = tk.Button(self, 
              compound=tk.CENTER,
              padx = px,
              pady=py, 
              font = fnt,
              command=lambda: controller.show_frame(PageTrain),
              text='Train').pack(side="left")
        test_bt = tk.Button(self, 
              compound=tk.CENTER,
              padx = px,
              pady=py, 
              font = fnt,
              command=lambda: controller.show_frame(PageTest),
              text='Test').pack(side="left")
        search_bt = tk.Button(self, 
              compound=tk.CENTER,
              padx = px,
              pady=py, 
              font = fnt,
              command=lambda: controller.show_frame(PageSearch),
              text='Search').pack(side="left")
        
        exit_bt = tk.Button(self, 
              compound=tk.BOTTOM,
              padx = px,
              pady=py, 
              font = fnt,
              text='Exit', command=controller.destroy).pack(side="right")


class PageTrain(tk.Frame):

    algo=''
    #algos = ('SIFT','ORB','SURF')

    @staticmethod
    def SIFT_step1(image,gpath):
          gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
          # Save the image to a file
          cv2.imwrite(gpath,gray)
          return gray
          # def step1 end
    @staticmethod
    def SIFT_step2(gray):
          sift = cv2.xfeatures2d.SIFT_create()
          return sift.detectAndCompute(gray, None)
          # def step2 end
    @staticmethod  
    def step3(kps):
      for k in kps:
        print("X,Y:{},Size:{},Angle:{}\n".format(k.pt,k.size,k.angle))
      # def step3 end  
      
    @staticmethod
    def trainFile(algo):
          print(algo)#algoCB.get())  

          if algo == "SIFT":
            path = ALGO+"/"+algo#algoCB.get()
            shutil.rmtree(path, ignore_errors=True)
            shutil.rmtree(TEMP, ignore_errors=True)
          
            os.makedirs(path);
            os.makedirs(TEMP);
          
            #Create Training File
            folders=os.listdir(DBASE)
            for folder in folders:
              files = os.listdir(DBASE+"/"+folder)
              print(files)
              for file in files:
                oldpath = DBASE+"/"+folder+"/"+file
                newtemppath = TEMP+"/"+folder+"_"+file
                newtempkppath = TEMP+"/"+folder+"_kp"+file
                newkeypath = path+"/"+folder+"_"+file
              
                image = cv2.imread(oldpath)
                gray = PageTrain.SIFT_step1(image,newtemppath)

                (kps, descs) = PageTrain.SIFT_step2(gray)
              
                index = []
                for point in kps:
                  temp = (point.pt, point.size, point.angle, point.response, point.octave, point.class_id) 
                  index.append(temp)

                # Dump the keypoints
                f = open(newkeypath, "wb")
                f.write(_pickle.dumps(index))
                f.close()

                #print("SIFT# kps: {}, descriptors: {}".format(len(kps), descs.shape))
                ####Read from keypoint file #####
                #im=cv2.imread(newtemppath)
                #f = open(newkeypath, "rb")
                #index = _pickle.loads(f.read())
                #f.close()

                #kp = []

                #for point in index:
                #  temp = cv2.KeyPoint(x=point[0][0],y=point[0][1],_size=point[1], _angle=point[2], 
                #              _response=point[3], _octave=point[4], _class_id=point[5]) 
                #  kp.append(temp)

                # Draw the keypoints
                #img = cv2.drawKeypoints(gray, kp, None, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
                #imm=cv2.drawKeypoints(im, kp);
                #cv2.imwrite(newtempkppath,img)
                #### END ######
              #


            tk.messagebox.showinfo("Algorithm", "Creating {} File".format(algo)) 
            # if end
          else :
            tk.messagebox.showinfo("Algorithm", "Sorry {} not implemented".format(algo))
          # def trainFile end   



    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        fnt1 = "Verdana 18 bold"
        fnt2 = "Verdana 12 bold"
        w1 = tk.Frame(self)
        w1.pack()
        w2 = tk.Frame(self)
        w2.pack()

        label = tk.Label(w1, font = fnt1,text="Train CBIR!!!")
        label.pack(pady=10,padx=10)
        
        tk.Label(w2, font = fnt2,text="Algorithm:").pack(side="left") 
        
        algo = tk.StringVar()
        
        algoCB = ttk.Combobox(w2, state="readonly")
        algoCB.config(values=ALGOS)
        algoCB.current(0) 
        #algoCB.pack()
        algoCB.pack(pady=10,padx=10,side="left")
        
        train_bt = tk.Button(self, font = fnt2,text="Train",command=lambda: PageTrain.trainFile(algoCB.get()))
        train_bt.pack()

        back_bt = tk.Button(self, text="Back to Home",font = fnt2,command=lambda: controller.show_frame(StartPage))
        back_bt.pack(side="bottom")

        # def __init__ end
    


class PageSearch(tk.Frame):

    d = {'key':'value'}
    m = {'key':'value'}
    c = {'key':'value'}
    cnt=0
    selfile=''
    selparent=''
    @staticmethod
    def orb_compute(file1,file2,result):

      img1 = cv2.imread(file1,0) # queryImage
      img2 = cv2.imread(file2,0) # trainImage

      # Initiate ORB detector
      orb = cv2.ORB_create()

      # find the keypoints and descriptors with ORB
      kp1, des1 = orb.detectAndCompute(img1,None)
      kp2, des2 = orb.detectAndCompute(img2,None)

      # create BFMatcher object
      bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

      # Match descriptors.
      matches = bf.match(des1,des2)

      # Sort them in the order of their distance.
      matches = sorted(matches, key = lambda x:x.distance)

      file = os.path.basename(file2)
      parent=os.path.basename(os.path.dirname(file2))
      PageSearch.m[file]= matches
      PageSearch.c[file]= parent
      if(len(matches)>= PageSearch.cnt):
        PageSearch.cnt=len(matches)
        PageSearch.selfile=file
        PageSearch.selcategory=parent

      print("{}<><><>{}<><><>{}".format(file2,len(matches),parent))


      # Draw first 10 matches.
      match_img = cv2.drawMatches(img1,kp1,img2,kp2,matches ,None, flags=2)

      #plt.imshow(match_img),plt.show()
      cv2.imwrite(result,match_img)
      
    @staticmethod
    def show_rgb_img(img):
      """Convenience function to display a typical color image"""
      return plt.imshow(cv2.cvtColor(img, cv2.CV_32S))

    @staticmethod
    def to_gray(color_img):
      gray = cv2.cvtColor(color_img, cv2.COLOR_BGR2GRAY)
      return gray

    @staticmethod
    def gen_sift_features(gray_img):
      sift = cv2.xfeatures2d.SIFT_create()
      # kp is the keypoints
      #
      # desc is the SIFT descriptors, they're 128-dimensional vectors
      # that we can use for our final features
      kp, desc = sift.detectAndCompute(gray_img, None)
      return kp, desc

    @staticmethod
    def show_sift_features(gray_img, color_img, kp):
      return plt.imshow(cv2.drawKeypoints(gray_img, kp, color_img.copy()))

    @staticmethod
    def sift_compute(file1,file2,result):
      

      img1 = cv2.imread(file1)
      img2 = cv2.imread(file2)
      #show_rgb_img(img1);
      #plt.show()

      img1_gray = PageTest.to_gray(img1)
      img2_gray = PageTest.to_gray(img2)

      #plt.imshow(img1_gray, cmap='gray'),plt.show();

      # generate SIFT keypoints and descriptors
      img1_kp, img1_desc = PageTest.gen_sift_features(img1_gray)
      img2_kp, img2_desc = PageTest.gen_sift_features(img2_gray)

      #print ('Here are what our SIFT features look like for the   image:')
      #show_sift_features(img1_gray, img1_front, img1_kp);
      #plt.show()

      # create a BFMatcher object which will match up the SIFT features
      bf = cv2.BFMatcher(cv2.NORM_L2, crossCheck=True)
      matches = bf.match(img1_desc, img2_desc)
      # Sort the matches in the order of their distance.
      matches = sorted(matches, key = lambda x:x.distance)
      file = os.path.basename(file2)
      parent=os.path.basename(os.path.dirname(file2))
      PageSearch.m[file]= matches
      PageSearch.c[file]= parent
      if(len(matches)>= PageSearch.cnt):
        PageSearch.cnt=len(matches)
        PageSearch.selfile=file
        PageSearch.selcategory=parent

      print("{}<><><>{}<><><>{}".format(file2,len(matches),parent))
      # draw the top N matches
      N_MATCHES = 100

      match_img = cv2.drawMatches( img1, img1_kp, img2, img2_kp, matches[:N_MATCHES], img2.copy(), flags=0)

      #plt.figure(figsize=(12,6))
      #plt.imshow(match_img);
      #plt.show()
      cv2.imwrite(result,match_img)

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        fnt1 = "Verdana 18 bold"
        fnt2 = "Verdana 12 bold"

        w1 = tk.Frame(self)
        w1.pack()
        w2 = tk.Frame(self)
        w2.pack()
        w3 = tk.Frame(self)
        w3.pack()
        w4 = tk.Frame(self)
        w4.pack()
        w5 = tk.Frame(self)
        w5.pack()
        
        v=tk.StringVar()
        
        label = tk.Label(w1, font = fnt1,text="Search CBIR!!!")
        label.pack(pady=10,padx=10)
        
        tk.Label(w2,font = fnt2,text="File:").pack(side="left") 
        filelabel = tk.Entry(w2,textvariable=v)
        filelabel.pack(pady=10,padx=10,side="left")
        
        def selFile():
          filename = askopenfilename()
          print(filename)
          v.set(filename)

        file_bt = tk.Button(w2, font = fnt2,text="Select",command=selFile)
        file_bt.pack(side="left")
        
        tk.Label(w3,font = fnt2,text="Algorithm:").pack(side="left") 

        folder = tk.StringVar()
        #algos = ('SIFT','ORB','SURF')
        
        algoCB = ttk.Combobox(w3, state="readonly")
        algoCB.config(values=ALGOS)
        algoCB.current(0) 
        algoCB.pack(pady=10,padx=10,side="left",fill="x")
        def onselect(evt):
          # Note here that Tkinter passes an event object to onselect()
          w = evt.widget
          index = int(w.curselection()[0])
          value = w.get(index)
          print ('You selected item {}: "{}"'.format(index, value))
          match_img = cv2.imread(PageSearch.d.get(value))
          plt.imshow(cv2.cvtColor(match_img, cv2.CV_32S));
          plt.show()

        lb1 = tk.Listbox(w5)
        lb1.bind('<<ListboxSelect>>', onselect)
        lb1.pack()
        def searchFile():
          lb1.delete(0,tk.END)
          PageSearch.cnt=0
          PageSearch.selfile=''
          PageSearch.selparent=''
          shutil.rmtree(TEMP, ignore_errors=True)
          os.makedirs(TEMP);
          
          your_file=v.get()
          print(your_file)
          timestamp = int(time.time()*1000.0)          
          new_file=str(timestamp)+"_"+os.path.basename(your_file)
          algo=algoCB.get()
         

          #print(new_folder)
          new_path=TEMP+"/"+new_file

          print(new_path)

          shutil.copy(your_file,new_path)
          #####################
          folders=os.listdir(DBASE)
          i=0
          for folder in folders:
            files = os.listdir(DBASE+"/"+folder)
            print(files)
            for file in files:
              oldpath = DBASE+"/"+folder+"/"+file
              PageSearch.d[file]= oldpath
              #lb1.insert(i, file)
              i = i+1
              ## ## ## ##
              filename, file_extension = os.path.splitext(oldpath)
              print(new_path)
              result_path = TEMP+"/"+algo+"_"+folder+"_res"+str(i)+file_extension
              if algo == "SIFT":
                PageSearch.sift_compute(new_path,oldpath,result_path)
              else:
                PageSearch.orb_compute(new_path,oldpath,result_path)
          lb1.insert(0, PageSearch.selfile)
            
          lb1.pack()

          ########################
          tk.messagebox.showinfo("Result", "Searching database using {} .Result={}"
                                    .format(algoCB.get(),PageSearch.selcategory))      
          
          v.set("")
          #else :
          #  tk.messagebox.showinfo("Algorithm", "Sorry {} not implemented".format(algo))

        search_bt = tk.Button(w4,font = fnt2,text="Search",command=searchFile)
        search_bt.pack()
        
        

        back_bt = tk.Button(self, text="Back to Home",font = fnt2,command=lambda: controller.show_frame(StartPage))
        back_bt.pack(side="bottom")
        # def __init__ end
       # def __init__ end
        
class PageAdd(tk.Frame):

    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        fnt1 = "Verdana 18 bold"
        fnt2 = "Verdana 12 bold"

        w1 = tk.Frame(self)
        w1.pack()
        w2 = tk.Frame(self)
        w2.pack()
        w3 = tk.Frame(self)
        w3.pack()

        v=tk.StringVar()

        label = tk.Label(w1, font = fnt1,text="Add To CBIR!!!")
        label.pack(pady=10,padx=10)
        
        tk.Label(w2,font = fnt2,text="File:").pack(side="left") 
        filelabel = tk.Entry(w2,textvariable=v)
        filelabel.pack(pady=10,padx=10,side="left")
        
        def selFile():
          filename = askopenfilename()
          print(filename)
          v.set(filename)

        file_bt = tk.Button(w2, font = fnt2,text="Select",command=selFile)
        file_bt.pack(side="left")
        
        tk.Label(w3,font = fnt2,text="Category:").pack(side="left") 

        folder = tk.StringVar()
        folders=os.listdir(DBASE)
        
        folderCB = ttk.Combobox(w3, state="readonly")
        folderCB.config(values=folders)
        folderCB.current(0) 
        folderCB.pack(pady=10,padx=10,side="left")

        def addFile():
          your_file=v.get()
          print(your_file)
          timestamp = int(time.time()*1000.0)          
          new_file=str(timestamp)+"_"+os.path.basename(your_file)
          new_folder=folderCB.get()
          
          print(new_folder)
          new_path=DBASE+"/"+new_folder+"/"+new_file

          print(new_path)

          shutil.copy(your_file,new_path)
          tk.messagebox.showinfo("Database", "Adding {} to {} database".format(new_file,folderCB.get()))      
          
          v.set("")


        add_bt = tk.Button(self,font = fnt2,text="Add",command=addFile)
        add_bt.pack()

        back_bt = tk.Button(self, text="Back to Home",font = fnt2,command=lambda: controller.show_frame(StartPage))
        back_bt.pack(side="bottom")
        # def __init__ end

class PageTest(tk.Frame):

    @staticmethod
    def orb_compute(file1,file2,result):

      img1 = cv2.imread(file1,0) # queryImage
      img2 = cv2.imread(file2,0) # trainImage

      # Initiate ORB detector
      orb = cv2.ORB_create()

      # find the keypoints and descriptors with ORB
      kp1, des1 = orb.detectAndCompute(img1,None)
      kp2, des2 = orb.detectAndCompute(img2,None)

      # create BFMatcher object
      bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

      # Match descriptors.
      matches = bf.match(des1,des2)

      # Sort them in the order of their distance.
      matches = sorted(matches, key = lambda x:x.distance)

      # Draw first 10 matches.
      match_img = cv2.drawMatches(img1,kp1,img2,kp2,matches ,None, flags=2)

      plt.imshow(match_img),plt.show()
      cv2.imwrite(result,match_img)

    @staticmethod
    def show_rgb_img(img):
      """Convenience function to display a typical color image"""
      return plt.imshow(cv2.cvtColor(img, cv2.CV_32S))

    @staticmethod
    def to_gray(color_img):
      gray = cv2.cvtColor(color_img, cv2.COLOR_BGR2GRAY)
      return gray

    @staticmethod
    def gen_sift_features(gray_img):
      sift = cv2.xfeatures2d.SIFT_create()
      # kp is the keypoints
      #
      # desc is the SIFT descriptors, they're 128-dimensional vectors
      # that we can use for our final features
      kp, desc = sift.detectAndCompute(gray_img, None)
      return kp, desc
    
    @staticmethod
    def show_sift_features(gray_img, color_img, kp):
      return plt.imshow(cv2.drawKeypoints(gray_img, kp, color_img.copy()))

    @staticmethod
    def sift_compute(file1,file2,result):
      img1 = cv2.imread(file1)
      img2 = cv2.imread(file2)
      #show_rgb_img(img1);
      #plt.show()

      img1_gray = PageTest.to_gray(img1)
      img2_gray = PageTest.to_gray(img2)

      #plt.imshow(img1_gray, cmap='gray'),plt.show();

      # generate SIFT keypoints and descriptors
      img1_kp, img1_desc = PageTest.gen_sift_features(img1_gray)
      img2_kp, img2_desc = PageTest.gen_sift_features(img2_gray)

      #print ('Here are what our SIFT features look like for the   image:')
      #show_sift_features(img1_gray, img1_front, img1_kp);
      #plt.show()

      # create a BFMatcher object which will match up the SIFT features
      bf = cv2.BFMatcher(cv2.NORM_L2, crossCheck=True)
      matches = bf.match(img1_desc, img2_desc)
      # Sort the matches in the order of their distance.
      matches = sorted(matches, key = lambda x:x.distance)
      # draw the top N matches
      N_MATCHES = 100

      match_img = cv2.drawMatches( img1, img1_kp, img2, img2_kp, matches[:N_MATCHES], img2.copy(), flags=0)

      plt.figure(figsize=(12,6))
      plt.imshow(match_img);
      plt.show()
      cv2.imwrite(result,match_img)



    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        w1 = tk.Frame(self)
        w1.pack()
        w2 = tk.Frame(self)
        w2.pack()
        w3 = tk.Frame(self)
        w3.pack()
        w4 = tk.Frame(self)
        w4.pack()
        
        fnt1 = "Verdana 18 bold"
        fnt2 = "Verdana 12 bold"

        v1=tk.StringVar()
        v2=tk.StringVar()

        label = tk.Label(w1,font = fnt1,text="Test CBIR!!!")
        label.pack(pady=10,padx=10)
        
        tk.Label(w2,font = fnt2,text="Algorithm:").pack(side="left") 
        
        folder = tk.StringVar()
        #algos = ('SIFT','ORB','SURF')
        
        algoCB = ttk.Combobox(w2, state="readonly")
        algoCB.config(values=ALGOS)
        algoCB.current(0) 
        algoCB.pack(pady=10,padx=10,side="left",fill="x")


        tk.Label(w3, font = fnt2,text="File1:").pack(side="left") 

        filelabel1 = tk.Entry(w3, textvariable=v1)
        filelabel1.pack(pady=10,padx=10,side="left")
        
        def selFile1():
          filename = askopenfilename()
          print(filename)
          v1.set(filename)

        

        file_bt1 = tk.Button(w3,font = fnt2,text="Select",command=selFile1)
        file_bt1.pack(side="left",fill="x")

        tk.Label(w4, font = fnt2,text="File2:").pack(side="left") 

        filelabel2 = tk.Entry(w4,textvariable=v2)
        filelabel2.pack(pady=10,padx=10,side="left")
        
        
        def selFile2():
          filename = askopenfilename()
          print(filename)
          v2.set(filename)


        file_bt2 = tk.Button(w4,font = fnt2,text="Select",command=selFile2)
        file_bt2.pack()
                
        def computeFile():
          your_file1 = v1.get()
          print(your_file1)
          
          your_file2 = v2.get()
          print(your_file2)
          
          timestamp = int(time.time()*1000.0)          
          
          new_file1 = str(timestamp)+"_"+os.path.basename(your_file1)
          new_file2 = str(timestamp)+"_"+os.path.basename(your_file2)
          
          algo = algoCB.get()          
          print(algo)

          shutil.rmtree(TEMP, ignore_errors=True)
          os.makedirs(TEMP);
        
          new_path1 = TEMP+"/"+new_file1
          print(new_path1)

          new_path2 = TEMP+"/"+new_file2

          shutil.copy(your_file1,new_path1)
          shutil.copy(your_file2,new_path2)
          
          filename, file_extension = os.path.splitext(new_path1)
          print(new_path2)
          result_path = TEMP+"/"+algo+"_res"+file_extension

          
          ##############################
          if algo == "ORB":
            PageTest.orb_compute(new_path1,new_path2,result_path)
            #tk.messagebox.showinfo("Test", "Computing {} to {} using {}".format(new_file1,new_file2,algoCB.get()))        

          elif algo == "SIFT":
            PageTest.sift_compute(new_path1,new_path2,result_path)

          else:
            tk.messagebox.showinfo("Test", "Algo not implemented")      
          ##############################
          
          
          v1.set("")
          v2.set("")


        compute_bt = tk.Button(self,font = fnt2,text="Compute",command=computeFile)
        compute_bt.pack()

        back_bt = tk.Button(self, text="Back to Home",font = fnt2,command=lambda: controller.show_frame(StartPage))
        back_bt.pack(side="bottom")
        # def __init__ end

app = CBIRUI()
app.mainloop()
