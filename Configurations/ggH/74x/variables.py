# variables

#variables = {}
    
#'fold' : # 0 = not fold (default), 1 = fold underflowbin, 2 = fold overflow bin, 3 = fold underflow and overflow
   
variables['events']  = {   'name': '1',      
                        'range' : (1,0,2),  
                        'xaxis' : 'events', 
                         'fold' : 3
                        }
    
#variables['mll']  = {   'name': 'mll',            #   variable name    
                        #'range' : (20,10,200),    #   variable range
                        #'xaxis' : 'm_{ll} [GeV]',  #   x axis name
                         #'fold' : 3
                        #}
                        
#variables['mth']  = {   'name': 'mth',            #   variable name    
                        #'range' : (20,0,400),    #   variable range
                        #'xaxis' : 'm_{T}^{H} [GeV]',  #   x axis name
                        #'fold' : 3
                        #}



#variables['mllVSmth'] = {   'name': 'mll:mth',            #   variable name    
                        #'range' : (10,0,200, 5,10,110),            #   variable range
                        #'xaxis' : 'm_{ll} : m_{T}^{H}',      #   x axis name
                        #'fold' : 3
                        #}


variables['mllVSmth'] = {   'name': 'mll:mth',            #   variable name    
                        'range' : (7,60,200, 5,10,110),            #   variable range
                        'xaxis' : 'm_{ll} : m_{T}^{H}',      #   x axis name
                        'fold' : 3 , 
                        # do weighted plot too
                        'doWeight' : 1,
                        'binX'     : 7,
                        'binY'     : 5
                        #
                        }



## just for fun plots:

#variables['nvtx']  = {   'name': 'nvtx',      
                        #'range' : (40,0,40),  
                        #'xaxis' : 'nvtx', 
                         #'fold' : 3
                        #}
                        
#variables['ptll']  = {   'name': 'ptll',            #   variable name    
                        #'range' : (20,0,200),    #   variable range
                        #'xaxis' : 'pt_{ll} [GeV]',  #   x axis name
                         #'fold' : 3
                        #}

#variables['met']  = {   'name': 'pfType1Met',            #   variable name    
                        #'range' : (20,0,200),    #   variable range
                        #'xaxis' : 'pfmet [GeV]',  #   x axis name
                         #'fold' : 0
                        #}
