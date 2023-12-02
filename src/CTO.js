import React, { useState } from 'react';
import './CTO.css';

const statusOptions = ['N/A', 'Draft', 'Develop', 'Review', 'Negotiate', 'Final'];

const facilityOptions = ['N/A', 'SLUH', 'CG', 'SM', 'DP'];

const contractOptions = ['N/A', 'Draft', 'Review', 'Negotiate', 'COI', 'Final', 'PI-Sign', 'PE', 'FE'];

const irbApprovalOptions = ['N/A', 'Submit', 'Approve', 'Suspend', 'Deferred'];

const projectTypeOptions = ['Ind', 'Ind-Amd', 'Grant', 'Grant-Amd', 'PI-I', 'PI-I-Amd'];

const ctoWDGrantSetupOptions = ['N/A', 'Request', 'Assign', 'Notify', 'Complete'];

const ctoIDXSetupOptions = ['N/A', 'Request', 'Receive', 'Setup', 'Notify', 'Complete'];

const ideIndOptions = ['N/A', 'Request', 'Complete'];

const consentFormOptions = ['N/A', 'Request', 'Draft'];

const studyFeasibilityOptions = ['N/A', 'Request', 'Completed'];

const CTO = () => {
  const [ctoBudget, setCTOBudget] = useState('N/A');
  const [ctoCA, setCTOCA] = useState('N/A');
  const [ssmFacility, setSSMFacility] = useState('N/A');
  const [contracts, setContracts] = useState('N/A');
  const [ssmRBRApproval, setSSMRBRApproval] = useState('N/A');
  const [ctoCTMS, setCTOCTMS] = useState('N/A');
  const [ctoIRBChecklist, setCTOIRBChecklist] = useState('N/A');
  const [irbApproval, setIRBApproval] = useState('N/A');
  const [projectType, setProjectType] = useState('Ind');
  const [status, setStatus] = useState('Active');
  const [ctoWDGrantSetup, setCTOWDGrantSetup] = useState('N/A');
  const [ctoIDXSetup, setCTOIDXSetup] = useState('N/A');
  const [ideInd, setIDEIND] = useState('N/A');
  const [consentForm, setConsentForm] = useState('N/A');
  const [studyFeasibility, setStudyFeasibility] = useState('N/A');
  const [origSubmitDate, setOrigSubmitDate] = useState('');
  const [irbSubmitDate, setIRBSubmitDate] = useState('');
  const [pauseDate, setPauseDate] = useState('');
  const [restartDate, setRestartDate] = useState('');
  const [estStartDate, setEstStartDate] = useState('');
  const [eRSWD, setERSWD] = useState('');
  const [irb, setIRB] = useState('');


  return (
    <div className="cto-container">
      <div className="left-container">
        <h2>CTO Track</h2>

        <label>
          IRB Submit Date:
          <input
            type="text"
            name="irbSubmitDate"
            value={irbSubmitDate}
            onChange={(e) => setIRBSubmitDate(e.target.value)}
          />
        </label>

        <label>
          eRS/WD:
          <input
            type="text"
            name="eRSWD"
            value={eRSWD}
            onChange={(e) => setERSWD(e.target.value)}
          />
        </label>

        <label>
          IRB:
          <input
            type="text"
            name="irb"
            value={irb}
            onChange={(e) => setIRB(e.target.value)}
          />
        </label>
        </div>
      <div className="middle-container">
      <label>
          CTO Budget:
          <select value={ctoBudget} onChange={(e) => setCTOBudget(e.target.value)}>
            {statusOptions.map((option) => (
              <option key={option} value={option}>
                {option}
              </option>
            ))}
          </select>
        </label>

      <label>
        CTO Budget:
        <select value={ctoBudget} onChange={(e) => setCTOBudget(e.target.value)}>
          {statusOptions.map((option) => (
            <option key={option} value={option}>
              {option}
            </option>
          ))}
        </select>
      </label>

      <label>
        CTO CA:
        <select value={ctoCA} onChange={(e) => setCTOCA(e.target.value)}>
          {statusOptions.map((option) => (
            <option key={option} value={option}>
              {option}
            </option>
          ))}
        </select>
      </label>

      <label>
        SSM Facility:
        <select value={ssmFacility} onChange={(e) => setSSMFacility(e.target.value)}>
          {facilityOptions.map((option) => (
            <option key={option} value={option}>
              {option}
            </option>
          ))}
        </select>
      </label>

      <label>
        Contracts:
        <select value={contracts} onChange={(e) => setContracts(e.target.value)}>
          {contractOptions.map((option) => (
            <option key={option} value={option}>
              {option}
            </option>
          ))}
        </select>
      </label>

      <label>
        IRB Approval:
        <select value={irbApproval} onChange={(e) => setIRBApproval(e.target.value)}>
          {irbApprovalOptions.map((option) => (
            <option key={option} value={option}>
              {option}
            </option>
          ))}
        </select>
      </label>

      <label>
        Project Type:
        <select value={projectType} onChange={(e) => setProjectType(e.target.value)}>
          {projectTypeOptions.map((option) => (
            <option key={option} value={option}>
              {option}
            </option>
          ))}
        </select>
      </label>

      <label>
        Status:
        <select value={status} onChange={(e) => setStatus(e.target.value)}>
          {statusOptions.map((option) => (
            <option key={option} value={option}>
              {option}
            </option>
          ))}
        </select>
      </label>

      <label>
        CTO WD Grant Set-Up:
        <select value={ctoWDGrantSetup} onChange={(e) => setCTOWDGrantSetup(e.target.value)}>
          {ctoWDGrantSetupOptions.map((option) => (
            <option key={option} value={option}>
              {option}
            </option>
          ))}
        </select>
      </label>

      <label>
        CTO IDX Set-Up:
        <select value={ctoIDXSetup} onChange={(e) => setCTOIDXSetup(e.target.value)}>
          {ctoIDXSetupOptions.map((option) => (
            <option key={option} value={option}>
              {option}
            </option>
          ))}
        </select>
      </label>

      <label>
        IDE / IND:
        <select value={ideInd} onChange={(e) => setIDEIND(e.target.value)}>
          {ideIndOptions.map((option) => (
            <option key={option} value={option}>
              {option}
            </option>
          ))}
        </select>
      </label>

      <label>
        Consent Form:
        <select value={consentForm} onChange={(e) => setConsentForm(e.target.value)}>
          {consentFormOptions.map((option) => (
            <option key={option} value={option}>
              {option}
            </option>
          ))}
        </select>
      </label>

      <label>
        Study Feasibility:
        <select value={studyFeasibility} onChange={(e) => setStudyFeasibility(e.target.value)}>
          {studyFeasibilityOptions.map((option) => (
            <option key={option} value={option}>
              {option}
            </option>
          ))}
        </select>
      </label>
      </div>
      <div className="right-container">
        <h2>CTO Information</h2>
        <label>
          Orig. Submit Date:
          <input
            type="text"
            name="origSubmitDate"
            value={origSubmitDate}
            onChange={(e) => setOrigSubmitDate(e.target.value)}
          />
        </label>

        <label>
          IRB Submit Date:
          <input
            type="text"
            name="irbSubmitDate"
            value={irbSubmitDate}
            onChange={(e) => setIRBSubmitDate(e.target.value)}
          />
        </label>

        <label>
          Pause Date:
          <input
            type="text"
            name="pauseDate"
            value={pauseDate}
            onChange={(e) => setPauseDate(e.target.value)}
          />
        </label>

        <label>
          Restart Date:
          <input
            type="text"
            name="restartDate"
            value={restartDate}
            onChange={(e) => setRestartDate(e.target.value)}
          />
        </label>

        <label>
          Est. Start Date:
          <input
            type="text"
            name="estStartDate"
            value={estStartDate}
            onChange={(e) => setEstStartDate(e.target.value)}
          />
        </label>
        </div>
    </div>
  );
};

export default CTO;