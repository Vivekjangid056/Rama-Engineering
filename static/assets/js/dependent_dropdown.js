document.addEventListener('DOMContentLoaded', function () {
    const dropdownItems = document.querySelectorAll('.dropdown-item');
    const menuContent = document.getElementById('menu-content');


    const menuData = {
        'system-settings': `
        <li class="menu-title" key="t-menu">System Settings</li>
            <a href="${urls.instituteList}" class="waves-effect fw-bold">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Institute Profile</span>
            </a>
            <a href="${urls.branchList}" class="waves-effect fw-bold">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Branches</span>
            </a>
            <a href="${urls.appIcons}" class="waves-effect fw-bold">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">App Icons</span>
            </a>
            <a href="${urls.appBanners}" class="waves-effect fw-bold">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">App Banners</span>
            </a>
            <a href="javascript: void(0);" class="fw-bold waves-effect sidebar-link d-flex justify-content-between align-items-center" data-bs-toggle="collapse"  data-bs-target="#system-settings-list-of-masters" aria-expanded="false" aria-controls="pages">
            <div>
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">List of Masters</span>
            </div>
                <i class="fa fa-chevron-left collapse-chevron"></i>
            </a>
            <ul id="system-settings-list-of-masters" class="sidebar-dropdown list-unstyled collapse" data-bs-parent="#accordionExample">
                <li class="sidebar-item">
                    <a href="${urls.listOfCaste}"><i class="fas fa-user-tag"></i>Caste</a>
                </li>
                <li class="sidebar-item">
                    <a href="${urls.listOfCategory}"><i class="fas fa-layer-group"></i>Category</a>
                </li>
                <li class="sidebar-item">
                    <a href="${urls.listOfHouse}"><i class="fas fa-home"></i>House</a>
                </li>
                <li class="sidebar-item">
                    <a href="${urls.listOfMedium}"><i class="fas fa-book-open"></i>Medium</a>
                </li>
                <li class="sidebar-item">
                    <a href="${urls.listOfReligion}"><i class="fas fa-praying-hands"></i>Religion</a>
                </li>
                <li class="sidebar-item">
                    <a href="${urls.listOfReference}"><i class="fas fa-book"></i>Reference</a>
                </li>
                <li class="sidebar-item">
                    <a href="${urls.listOfNationality}"><i class="fas fa-globe"></i>Nationality</a>
                </li>
                <li class="sidebar-item">
                    <a href="${urls.listOfMotherTongue}"><i class="fas fa-language"></i>Mother Tongue</a>
                </li>
                <li class="sidebar-item">
                    <a href="${urls.listOfFamilyRelation}"><i class="fas fa-users"></i>Family Relation</a>
                </li>
                <li class="sidebar-item">
                    <a href="${urls.listOfEnquiryType}"><i class="fas fa-question-circle"></i>Enquiry Type</a>
                </li>
                <li class="sidebar-item">
                    <a href="${urls.listOfPaymentMode}"><i class="fas fa-money-bill"></i>Payment Mode</a>
                </li>
                <li class="sidebar-item">
                    <a href="${urls.listOfStandard}"><i class="fas fa-chalkboard-teacher"></i>Class</a>
                </li>
                <li class="sidebar-item">
                    <a href="${urls.listOfSubject}"><i class="fas fa-book-reader"></i>Subject</a>
                </li>
                <li class="sidebar-item">
                    <a href="${urls.listOfDocument}"><i class="fas fa-folder-open"></i>Documents</a>
                </li>
                <li class="sidebar-item">
                    <a href="${urls.listOfFeeHeads}"><i class="fas fa-file-invoice-dollar"></i>Fee Heads</a>
                </li>
                <li class="sidebar-item">
                    <a href="${urls.listOfNameOfBank}"><i class="fas fa-university"></i>Name of the Bank</a>
                </li>
                <li class="sidebar-item">
                    <a href="${urls.listOfStudentType}"><i class="fas fa-user-tag"></i>Student Type</a>
                </li>
                <li class="sidebar-item">
                    <a href="${urls.listOfChildStatus}"><i class="fas fa-user-tag"></i>Child Status</a>
                </li>
            </ul>
            <a href="#" class="fw-bold waves-effect sidebar-link d-flex justify-content-between align-items-center" data-bs-toggle="collapse"  data-bs-target="#system-settings-session-settings" aria-expanded="false" aria-controls="pages">
            <div>
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Session Settings</span>
            </div>
                <i class="fa fa-chevron-left collapse-chevron"></i>
            </a>
            <ul id="system-settings-session-settings" class="sidebar-dropdown list-unstyled collapse" data-bs-parent="#accordionExample">
                <li class="sidebar-item">
                    <a href="${urls.classWiseSubjects}"><i class="fas fa-signature"></i>Subjects for Class Groups</a>
                </li>
                <li class="sidebar-item">
                    <a href="${urls.discountSection}"><i class="fas fa-globe"></i>Discount Scheme</a>
                </li>
                <li class="sidebar-item">
                    <a href="${urls.section}"><i class="fas fa-layer-group"></i>Section</a>
                </li>
                <li class="sidebar-item ">
                    <a href="${urls.sessionCreate}"><i class="fas fa-user-tag"></i>Session Create</a>
                </li>
            </ul>
            <a href="${urls.listOfRoles}" class="waves-effect fw-bold">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">create roles</span>
            </a>
            <a href="${urls.sendSms}" class="waves-effect fw-bold">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">SMS Templates</span>
            </a>
            <a href="${urls.gallery}" class="waves-effect fw-bold">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Gallery</span>
            </a>
            <a href="${urls.customMenu}" class="waves-effect fw-bold">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Custom Menu</span>
            </a>
            <a href="${urls.enquiryList}" class="waves-effect fw-bold">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Enquiry</span>
            </a>
            <a href="${urls.promoteStudentsToNextStandard}" class="waves-effect fw-bold">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Student Promotion</span>
            </a>
        `
        ,
        'scholar-register': `
        <li class="menu-title" key="t-menu">scholar-register</li>
            <a href="${urls.studentRegistration}" class="waves-effect fw-bold">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Student</span>
            </a>
        `
        ,
        'fees-module': `
        <li class="menu-title" key="t-menu">Fees Module</li>
            <a href="${urls.feeList}" class="waves-effect fw-bold">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Fee Deposit</span>
            </a>
            <a href="${urls.additionalFeesInfo}" class="waves-effect fw-bold">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Additional Fees Info</span>
            </a>
            <a href="${urls.feeStructure}" class="waves-effect fw-bold">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Fees Structure</span>
            </a>
            <a href="${urls.paymentSchedule}" class="waves-effect fw-bold">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Installment Schedule</span>
            </a>
        `,
        'teacher-management': `
        <li class="menu-title" key="t-menu">Teacher Management</li>
            <a href="javascript: void(0)" class="fw-bold waves-effect sidebar-link d-flex justify-content-between align-items-center" data-bs-toggle="collapse"  data-bs-target="#teacher-management-list-master" aria-expanded="false" aria-controls="pages">
            <div>
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">List Master</span>
            </div>
                <i class="fa fa-chevron-left collapse-chevron"></i>
            </a>
            <ul id="teacher-management-list-master" class="sidebar-dropdown list-unstyled collapse" data-bs-parent="#accordionExample">
                <li class="sidebar-item">
                    <a href="${urls.categoryMasterList}"><i class="fas fa-signature"></i>Catagory Master</a>
                </li>
                <li class="sidebar-item ">
                    <a href="${urls.designationMasterList}"><i class="fas fa-user-tag"></i>Designation Master</a>
                </li>
                <li class="sidebar-item">
                    <a href="${urls.departmentMasterList}"><i class="fas fa-layer-group"></i>Department Master</a>
                </li>
                <li class="sidebar-item">
                    <a href="${urls.attendanceType}"><i class="fas fa-book-open"></i>Attendance Type</a>
                </li>
                <li class="sidebar-item">
                    <a href="${urls.holidayList}"><i class="fas fa-book-open"></i>Holiday List</a>
                </li>
            </ul>
            <a href="${urls.attendance}" class="waves-effect fw-bold">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Student's Attendance</span>
            </a>
            <a href="${urls.listOfEmployees}" class="waves-effect fw-bold">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Employee Master</span>
            </a>
            <a href="${urls.scheduleTimeTable}" class="waves-effect fw-bold">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Time Table</span>
            </a>
            <a href="${urls.classPeriods}" class="waves-effect fw-bold">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Class Periods</span>
            </a>
            <a href="${urls.studentIdList}" class="waves-effect fw-bold">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Student Id Card</span>
            </a>
            <a href="${urls.teacherIdList}" class="waves-effect fw-bold">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Teacher Id Card</span>
            </a>
        `,
        'hr': `
        <li class="menu-title" key="t-menu">HR</li>
            <a href="${urls.employeeAttendance}" class="waves-effect fw-bold">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Employee's Attendance</span>
            </a>
            <a href="#" class="fw-bold waves-effect sidebar-link d-flex justify-content-between align-items-center" data-bs-toggle="collapse"  data-bs-target="#hr-leave" aria-expanded="false" aria-controls="pages">
            <div>
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Leave</span>
            </div>
                <i class="fa fa-chevron-left collapse-chevron"></i>
            </a>
            <ul id="hr-leave" class="sidebar-dropdown list-unstyled collapse" data-bs-parent="#accordionExample">
                <li class="sidebar-item">
                    <a href="${urls.leaveTypes}"><i class="fas fa-signature"></i>My Leave Types</a>
                </li>
                <li class="sidebar-item ">
                    <a href="${urls.leaveApplications}"><i class="fas fa-user-tag"></i>Leave Applications</a>
                </li>
                <li class="sidebar-item ">
                    <a href="${urls.employeeListForLeaveBalance}"><i class="fas fa-user-tag"></i>Leave Balance</a>
                </li>
            </ul>
            <a href="#" class="fw-bold waves-effect sidebar-link d-flex justify-content-between align-items-center" data-bs-toggle="collapse"  data-bs-target="#hr-salary" aria-expanded="false" aria-controls="pages">
            <div>
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Salary</span>
            </div>
                <i class="fa fa-chevron-left collapse-chevron"></i>
            </a>
            <ul id="hr-salary" class="sidebar-dropdown list-unstyled collapse" data-bs-parent="#accordionExample">
                <li class="sidebar-item">
                    <a href="${urls.employeeSalaryDetails}"><i class="fas fa-signature"></i>Employee Salary Details</a>
                </li>
            </ul>
            <a href="${urls.hrInterviewList}" class="waves-effect fw-bold">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Interview</span>
            </a>
            <a href="${urls.teacherSubjectAssign}" class="waves-effect fw-bold">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Assign Subjects To Teacher</span>
            </a>
        `,
        'examination': `
        <li class="menu-title" key="t-menu">Examination</li>
            <a href="${urls.examTypeList}" class="waves-effect fw-bold">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Exam Type</span>
            </a>
            <a href="${urls.examTimeTable}" class="waves-effect fw-bold">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Exam Time Table</span>
            </a>
            <a href="${urls.gradingList}" class="waves-effect fw-bold">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Grading List</span>
            </a>
            <a href="${urls.examinationMarks}" class="waves-effect fw-bold">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Examination marks</span>
            </a>
            <a href="${urls.createExamResult}" class="waves-effect fw-bold">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Create Exam Result</span>
            </a>
            <a href="${urls.testMarks}" class="waves-effect fw-bold">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Test Marks</span>
            </a>
        `,
        'mess': `
        <li class="menu-title" key="t-menu">Mess</li>
            <a href="${urls.messOperatorList}" class="waves-effect fw-bold">
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">Mess Operator</span>
            </a>
            <a href="${urls.messDetails}" class="waves-effect fw-bold">
                <i class="bx bx-building"></i>
                <span key="t-dashboards">Mess Details</span>
            </a>
            <a href="${urls.messMenuItems}" class="waves-effect fw-bold">
                <i class='bx bx-food-menu'></i>
                <span key="t-dashboards">Mess Menu</span>
            </a>
            <a href="${urls.messAttendance}" class="waves-effect fw-bold">
                <i class='bx bx-food-menu'></i>
                <span key="t-dashboards">Mess Attendance</span>
            </a>
            
        `,
        'hostel': `
        <li class="menu-title" key="t-menu">Hostel</li>
            <a href="#" class="fw-bold waves-effect sidebar-link d-flex justify-content-between align-items-center" data-bs-toggle="collapse"  data-bs-target="#hostel-hostel-settings" aria-expanded="false" aria-controls="pages">
            <div>
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards">hostel Settings</span>
            </div>
                <i class="fa fa-chevron-left collapse-chevron"></i>
            </a>
            <ul id="hostel-hostel-settings" class="sidebar-dropdown list-unstyled collapse" data-bs-parent="#accordionExample">
                <li class="sidebar-item">
                    <a href="${urls.hostelBuilding}"><i class="fas fa-signature"></i>Hostel Building</a>
                </li>
                <li class="sidebar-item">
                    <a href="${urls.floor}"><i class="fas fa-signature"></i>Hostel Floors</a>
                </li>
                <li class="sidebar-item">
                    <a href="${urls.room}"><i class="fas fa-signature"></i>Hostel Rooms</a>
                </li>
                <li class="sidebar-item">
                    <a href="${urls.room_allocation}"><i class="fas fa-signature"></i>Allocate Rooms</a>
                </li>
                
            </ul>
            <a href="#" class="fw-bold waves-effect sidebar-link d-flex justify-content-between align-items-center" data-bs-toggle="collapse"  data-bs-target="#students-management-settings" aria-expanded="false" aria-controls="pages">
            <div>
                <i class="bx bx-home-circle"></i>
                <span key="t-dashboards"> In - Out Management </span>
            </div>
                <i class="fa fa-chevron-left collapse-chevron"></i>
            </a>
            <ul id="students-management-settings" class="sidebar-dropdown list-unstyled collapse" data-bs-parent="#accordionExample">
                <li class="sidebar-item">
                    <a href="${urls.std_hostel_in_out}"><i class="fas fa-signature"></i>Student In-Out</a>
                </li>
                
            </ul>
            <ul id="students-management-settings" class="sidebar-dropdown list-unstyled collapse" data-bs-parent="#accordionExample">
                <li class="sidebar-item">
                    <a href="${urls.guardian_hostel_in_out}"><i class="fas fa-signature"></i>Guardian In-Out</a>
                </li>
            </ul>
            
        `,
    };

    function initializeChevronToggle() {
        $('[data-bs-toggle="collapse"]').each(function () {
            var target = $(this).attr('data-bs-target');
            $(target).on('show.bs.collapse', function () {
                $(this).prev('a').find('.collapse-chevron').removeClass('fa-chevron-left').addClass('fa-chevron-down');
            }).on('hide.bs.collapse', function () {
                $(this).prev('a').find('.collapse-chevron').removeClass('fa-chevron-down').addClass('fa-chevron-left');
            });
        });
    }

    // Load sidebar state from localStorage
    const savedMenuKey = localStorage.getItem('sidebarMenuKey');
    if (savedMenuKey && menuData[savedMenuKey]) {
        menuContent.innerHTML = menuData[savedMenuKey];
    } else {
        // Set default menu content if no state is saved
        const defaultMenu = 'system-settings'; // Set this to the default menu you want to show
        if (menuData[defaultMenu]) {
            menuContent.innerHTML = menuData[defaultMenu];
        }
    }

    // Reinitialize chevron toggle after setting content
    initializeChevronToggle();

    // Add event listeners to dropdown items
    dropdownItems.forEach(item => {
        item.addEventListener('click', function (event) {
            event.preventDefault();
            const menuKey = this.getAttribute('data-menu');
            if (menuData[menuKey]) {
                menuContent.innerHTML = menuData[menuKey];
                // Save the selected menu key to localStorage
                localStorage.setItem('sidebarMenuKey', menuKey);
                initializeChevronToggle(); // Reinitialize the chevron toggle function after updating the content
            }
        });
    });
});