//
//---- generic 2D plot
//

void Draw2DImproved(std::string xName = "r_{1}", std::string yName = "r_{3}", std::string xNameVar = "r1", std::string yNameVar = "r3" , int dimension = 2 ) {
  
  TCanvas* cc = new TCanvas ("cc","",800,600); 
  
  TString whatToDraw = Form ("2*deltaNLL:%s:%s", xNameVar.c_str(), yNameVar.c_str());

  int n =  limit->Draw(whatToDraw.Data(),"deltaNLL<10","goff");
  
  TGraph2D *graphScan = new TGraph2D(n,limit->GetV2(),limit->GetV3(),limit->GetV1());
  graphScan->SetTitle("");
  graphScan->SetMarkerStyle(21);
  graphScan->SetMarkerColor(kRed);
  graphScan->SetLineColor(kRed);

  graphScan->Draw("colz");

  graphScan->GetXaxis()->SetTitle(xName.c_str());
  graphScan->GetYaxis()->SetTitle(yName.c_str());
  graphScan->GetZaxis()->SetTitle("- 2#Delta logL");
  graphScan->GetZaxis()->SetRangeUser(0,10);
  
//   graphScan->Draw("surf1");

  //---- 2D likelihood thresholds
  Double_t contours[2];
  if (dimension == 2) {
    contours[0] = 1;
    contours[1] = 3.84;
  }
  if (dimension == 3) {
    contours[0] = 3.67 / 2;
    contours[1] = 11.36 / 2;
  }
  
//   graphScan->Draw("cont4z");
  graphScan->Draw("colz");
  graphScan->GetHistogram()->GetXaxis()->SetTitle(xName.c_str());
  graphScan->GetHistogram()->GetYaxis()->SetTitle(yName.c_str());
  graphScan->GetHistogram()->GetZaxis()->SetTitle("- 2#Delta logL");
// //   graphScan->Draw("cont4z");
  graphScan->Draw("colz");
  

  TCanvas* cc2 = new TCanvas ("cc2","",800,600); 
  cc2->SetRightMargin(0.15);

  graphScan->Draw("colz");
  
  TH2F* HistStreamFn_ph2 = (TH2F*) (graphScan->GetHistogram())->Clone("testhisto_ph2");
  HistStreamFn_ph2->SetContour(2, contours);
  HistStreamFn_ph2->SetLineWidth(2);
  HistStreamFn_ph2->SetLineStyle(2);
  HistStreamFn_ph2->Draw("CONT1 LIST SAME");
  
//   gStyle->SetPadRightMargin(0.2);
  
  cc2->SetGrid();
  
  
}


