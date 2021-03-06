# cuts

supercut = ' mll > 12 \
          && Lepton_pt[0]>25 \
          && Lepton_pt[1]>10 \
          && (abs(Lepton_pdgId[1])==13 || Lepton_pt[1]>13) \
          && (nLepton>=2 && Alt$(Lepton_pt[2],0)<10) \
          && abs(Lepton_eta[0])<2.5 && abs(Lepton_eta[1])<2.5 \
          && ptll>30 \
          && PuppiMET_pt > 20 \
          && topcr \
          && 2jVBF \
          && hww_DYmvaDNN_VBF(Entry$) > 0.8 \
           '               

cuts['2j_VBF_ee_in'] = '(Lepton_pdgId[0]*Lepton_pdgId[1] == -11*11) \
                  && fabs(91.1876 - mll) < 7.5  \
               '

cuts['2j_VBF_uu_in'] = '(Lepton_pdgId[0]*Lepton_pdgId[1] == -13*13) \
                  && fabs(91.1876 - mll) < 7.5  \
               '

cuts['2j_VBF_df_in'] = '(Lepton_pdgId[0]*Lepton_pdgId[1] == -11*13) \
                  && fabs(91.1876 - mll) < 7.5  \
               '

cuts['2j_VBF_ee_out'] = '(Lepton_pdgId[0]*Lepton_pdgId[1] == -11*11) \
                  && fabs(91.1876 - mll) > 15  \
               '

cuts['2j_VBF_uu_out'] = '(Lepton_pdgId[0]*Lepton_pdgId[1] == -13*13) \
                  && fabs(91.1876 - mll) > 15  \
               '

cuts['2j_VBF_df_out'] = '(Lepton_pdgId[0]*Lepton_pdgId[1] == -11*13) \
                  && fabs(91.1876 - mll) > 15  \
               '
