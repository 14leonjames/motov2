import cv2
import numpy as np
# import latest 




def trip():

    #Load YOLO Algorithm
    net=cv2.dnn.readNet("yolov4-tiny-custom_final.weights","yolov4-tiny-custom.cfg")
    #To load all objects that have to be detected
    classes=[]
    with open("classes.names","r") as f:
        read=f.readlines()
    for i in range(len(read)):
        classes.append(read[i].strip("\n"))
    #Defining layer names
    layer_names=net.getLayerNames()
    output_layers=[]
    for i in net.getUnconnectedOutLayers():
        output_layers.append(layer_names[i[0]-1])
    print(layer_names)
    print(output_layers)
    #Loading the Image
    img=cv2.imread("img.jpg")
    height,width,channels=img.shape
    #Extracting features to detect objects
    blob=cv2.dnn.blobFromImage(img,0.00392,(416,416),(0,0,0),True,crop=False)
                                                            #Inverting blue with red
                                                            #bgr->rgb
    #We need to pass the img_blob to the algorithm
    net.setInput(blob)
    outs=net.forward(output_layers)
    #print(outs)
    #Displaying informations on the screen
    class_ids=[]
    confidences=[]
    boxes=[]
    for output in outs:
        for detection in output:
            #Detecting confidence in 3 steps
            scores=detection[5:]                #1
            class_id=np.argmax(scores)    #2
                
            confidence =scores[class_id]        #3
            if confidence >0.5: #Means if the object is detected
                center_x=int(detection[0]*width)
                center_y=int(detection[1]*height)
                w=int(detection[2]*width)
                h=int(detection[3]*height)
                #Drawing a rectangle
                x=int(center_x-w/2) # top left value
                y=int(center_y-h/2) # top left value
                boxes.append([x,y,w,h])
                confidences.append(float(confidence))
                class_ids.append(class_id)
            #cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
    #Removing Double Boxes
    indexes=cv2.dnn.NMSBoxes(boxes,confidences,0.3,0.4)
    nohel = []
    bike = []


    def rectContains(rect,pt):
        logic = rect[0] < pt[0] < rect[0]+rect[2] and rect[1] < pt[1] < rect[1]+rect[3]
        return logic

    for i in range(len(boxes)):
        if i in indexes:
            x, y, w, h = boxes[i]
            label = classes[class_ids[i]]  # name of the objects
            if label == "no-helmet":
            # image = img[y:y+h,x:x+w]
            # cv2.imwrite("cd6.jpg", image
                cx = x + w // 2
                cy = y + h // 2
                a1, a2 = cx , cy + (h //2)
                nohel.append([a1,a2])
                print(a1,a2)
    # Draw a circle in the center of rectangle
                #cv2.circle(img=img, center=(a1, a2), radius=3, color=(0, 255, 0), thickness=3)
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
                cv2.putText(img, label, (x, y), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 255), 2)
            if label == "bike":
                # logic = x < nohel[i][0] < x+w and y < nohel[i][1]< y+h
                # print(logic)
                print(x,y,x+w,y+h)
                bike.append([x,y,x+w,y+h]) 
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
                cv2.putText(img, label, (x, y), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 255), 2)
        
            
            for i in bike:
                c=0
                for j in nohel:
                    
                    rect = (i[0],i[1],i[2],i[3])
                    pt = [j[0],j[1]]
                    if(rectContains(rect,pt)):
                        # latest_file = latest.find_latest()
                        # q = latest_file.split("_")[1]
                        image = img[i[1]:i[3],i[0]:i[2]]
                        c+=1
                    print(c)
                    if(c>=3):
                        print("violated")
                        cv2.putText(img, "Triples", (20, 30), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 255), 2)
                        # cv2.imwrite("crop/cd_0_.jpg", image)
                        cv2.imwrite(f"cd_1_.jpg",image)

                    
                    
        

        

    cv2.imshow("Output",img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# triple()