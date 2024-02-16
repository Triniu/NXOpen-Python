import NXOpen
import NXOpen.Annotations

def main() : 

    theSession  = NXOpen.Session.GetSession()
    workPart = theSession.Parts.Work
    displayPart = theSession.Parts.Display

    obj=workPart.Views.WorkView.AskVisibleObjects() #### Get all visible object on a screen

    ann=[]
    for x in obj:
        if "Dimension" in str(x):
            if x.IsRetained==True: 
                ann.append(x)

    theSession.DisplayManager.BlankObjects(ann)
    workPart.Views.WorkView.FitAfterShowOrHide(NXOpen.View.ShowOrHideType.HideOnly)



if __name__ == '__main__':
    main()
