(window.webpackJsonpwebsbor2=window.webpackJsonpwebsbor2||[]).push([[0],{43:function(e,a,t){e.exports=t(72)},50:function(e,a,t){},72:function(e,a,t){"use strict";t.r(a);var n=t(0),l=t.n(n),r=t(37),c=t.n(r),m=(t(48),t(49),t(50),t(6)),s=t(13),o=t(15),i=t(16),u=t(18),d=t(17),h=t(19),E=t(73),p=t(74),v=t(75),f=t(12),g=t.n(f),b=function(e){function a(e){var t;return Object(o.a)(this,a),(t=Object(u.a)(this,Object(d.a)(a).call(this,e))).state={cardList:[]},t}return Object(h.a)(a,e),Object(i.a)(a,[{key:"componentDidMount",value:function(){var e=this;g.a.get("/api/groups?hash=hv123").then((function(a){200===a.status&&e.setState({cardList:a.data?a.data:[]})}))}},{key:"render",value:function(){var e=this.state.cardList;return l.a.createElement("div",{className:"site-wrapper"},l.a.createElement("nav",{className:"gov-nav"},l.a.createElement("div",{className:"wrapper"},l.a.createElement("div",{className:"subnav"},"\u0414\u0440\u0443\u0433\u0438\u0435 \u0441\u0430\u0439\u0442\u044b \u0440\u0435\u0441\u043f\u0443\u0431\u043b\u0438\u043a\u0438"),l.a.createElement("div",{className:"spacer"}),l.a.createElement("div",{className:"translate-menu"},"Rissian"),l.a.createElement(m.b,{to:"/cabinet",className:"auth"},"\u041b\u0438\u0447\u043d\u044b\u0439 \u043a\u0430\u0431\u0438\u043d\u0435\u0442"))),l.a.createElement("div",{className:"top-part"},l.a.createElement("div",{className:"wrapper"},l.a.createElement("header",{className:"site-header"},l.a.createElement("div",{className:"logo"},l.a.createElement("div",{className:"prime-text"},"\u0413\u043e\u0441\u0443\u0434\u0430\u0440\u0441\u0442\u0432\u0435\u043d\u043d\u044b\u0435 \u0443\u0441\u043b\u0443\u0433\u0438 ",l.a.createElement("br",null),l.a.createElement("span",null,"\u0420\u0435\u0441\u043f\u0443\u0431\u043b\u0438\u043a\u0438 \u0422\u0430\u0442\u0430\u0440\u0441\u0442\u0430\u043d"))),l.a.createElement("ul",{className:"help-nav"},l.a.createElement("li",null,l.a.createElement(m.b,{to:"/"},"\u041a\u0430\u0442\u0430\u043b\u043e\u0433 \u0443\u0441\u043b\u0443\u0433")),l.a.createElement("li",null,l.a.createElement(m.b,{to:"/"},"\u041f\u043e\u043c\u043e\u0449\u044c \u0438 \u043f\u043e\u0434\u0434\u0435\u0440\u0436\u043a\u0430")),l.a.createElement("li",null,l.a.createElement(m.b,{to:"/"},"\u041e\u043f\u043b\u0430\u0442\u0430"))),l.a.createElement("button",{type:"button",className:"mobile-menu-toggle"}))),l.a.createElement("div",{className:"wrapper"},l.a.createElement("div",{className:"main-search-form"},l.a.createElement(E.a,{for:"search-form",className:"sr-only"},"Email"),l.a.createElement(p.a,{type:"text",name:"email",id:"search-form",placeholder:"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0443\u0441\u043b\u0443\u0433\u0438"}),l.a.createElement(v.a,null,"\u041d\u0430\u0439\u0442\u0438 \u0443\u0441\u043b\u0443\u0433\u0443")),l.a.createElement("div",{className:"promo-columns"},l.a.createElement("div",{className:"column login-column"},l.a.createElement("div",{className:"icon"},l.a.createElement("img",{src:"/images/login-promo-icon.svg",alt:""})),l.a.createElement("div",{className:"column-content"},l.a.createElement("h3",null,"\u0412\u0445\u043e\u0434 \u0432 \u043b\u0438\u0447\u043d\u044b\u0439 \u043a\u0430\u0431\u0438\u043d\u0435\u0442"),l.a.createElement("p",null,"\u0412\u043e\u0439\u0434\u0438\u0442\u0435 \u0438\u043b\u0438 \u0437\u0430\u0440\u0435\u0433\u0438\u0441\u0442\u0440\u0438\u0440\u0443\u0439\u0442\u0435\u0441\u044c \u0447\u0442\u043e\u0431\u044b \u043f\u043e\u043b\u0443\u0447\u0438\u0442\u044c \u043f\u043e\u043b\u043d\u044b\u0439 \u0434\u043e\u0441\u0442\u0443\u043f \u043a \u044d\u043b\u0435\u043a\u0442\u0440\u043e\u043d\u043d\u044b\u043c \u0443\u0441\u043b\u0443\u0433\u0430\u043c"),l.a.createElement("a",{className:"btn btn-secondary first-btn",href:"https://digital.codedream.ru/admin/login/?next=/"},"\u0412\u043e\u0439\u0442\u0438"),l.a.createElement(v.a,{className:"second-btn"},"\u0417\u0430\u0440\u0435\u0433\u0438\u0441\u0442\u0440\u0438\u0440\u043e\u0432\u0430\u0442\u044c\u0441\u044f"))),l.a.createElement("div",{className:"column"},l.a.createElement("div",{className:"icon"}),l.a.createElement("div",{className:"column-content"},l.a.createElement("h3",null,"\u0423\u0432\u0435\u0434\u043e\u043c\u043b\u0435\u043d\u0438\u044f \u043e \u043d\u0430\u0447\u0438\u0441\u043b\u0435\u043d\u0438\u044f\u0445"),l.a.createElement("p",null,"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u0435 \u0434\u0430\u043d\u043d\u044b\u0435 \u0431\u0430\u043d\u043a\u043e\u0432\u0441\u043a\u043e\u0439 \u043a\u0430\u0440\u0442\u044b \u0438 \u043e\u043d\u0438 \u0431\u0443\u0434\u0443\u0442 \u0430\u0432\u0442\u043e\u043c\u0430\u0442\u0438\u0447\u0435\u0441\u043a\u0438 \u043f\u043e\u0434\u0441\u0442\u0430\u0432\u043b\u044f\u0442\u044c \u043f\u0440\u0438 \u043e\u043f\u043b\u0430\u0442\u0435")))))),l.a.createElement("div",{className:"bottom-part"},l.a.createElement("div",{className:"wrapper"},l.a.createElement("div",{className:"service-grid"},function(e){var a=e.map((function(e){return l.a.createElement(m.b,{to:"/service-request/".concat(e.id),className:"item",key:e.id},l.a.createElement("div",{className:"icon"},l.a.createElement("img",{src:e.icon,alt:""})),l.a.createElement("div",{className:"item-content"},l.a.createElement("div",{className:"item-title"},e.name),l.a.createElement("div",{className:"item-description"},e.description)))}));return a.length>0?l.a.createElement(n.Fragment,null,a):l.a.createElement(n.Fragment,null)}(e)))))}}]),a}(n.Component),y=t(14),N=t(8),F=t(76),O=t(77),C=t(78),j=t(79),w=t(80),k=t(81),_=t(82),x=t(83),P=t(5),S=t.n(P),D=t(41);function q(e,a){var t=Object.keys(e);if(Object.getOwnPropertySymbols){var n=Object.getOwnPropertySymbols(e);a&&(n=n.filter((function(a){return Object.getOwnPropertyDescriptor(e,a).enumerable}))),t.push.apply(t,n)}return t}function T(e){for(var a=1;a<arguments.length;a++){var t=null!=arguments[a]?arguments[a]:{};a%2?q(t,!0).forEach((function(a){Object(y.a)(e,a,t[a])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(t)):q(t).forEach((function(a){Object.defineProperty(e,a,Object.getOwnPropertyDescriptor(t,a))}))}return e}var R=t.n(D).a.pluralize,I=function(e){function a(e){var t;return Object(o.a)(this,a),(t=Object(u.a)(this,Object(d.a)(a).call(this,e))).state={activeTab:"1",formFields:{first_name:"",second_name:"",third_name:"",email:"",phone:"",inn:"",snils:"",passport:""},userRequests:[]},t.toggle=t.toggle.bind(Object(N.a)(t)),t.handleChangeField=t.handleChangeField.bind(Object(N.a)(t)),t}return Object(h.a)(a,e),Object(i.a)(a,[{key:"toggle",value:function(e){this.state.activeTab!==e&&this.setState({activeTab:e})}},{key:"handleChangeField",value:function(e,a){var t=this.state.formFields;this.setState({formFields:T({},t,Object(y.a)({},a,e.target.value))})}},{key:"componentDidMount",value:function(){var e=this;g.a.get("/api/client?hash=hv123").then((function(a){200===a.status&&e.setState({formFields:{first_name:a.data.first_name,last_name:a.data.last_name,father_name:a.data.third_name,email:a.data.email,phone:a.data.phone,inn:a.data.inn,snils:a.data.snils,passport:a.data.passport}})})),g.a.get("/api/requests?hash=hv123").then((function(a){200===a.status&&e.setState({userRequests:a.data?a.data:[]})}))}},{key:"render",value:function(){var e=this,a=this.state.userRequests;return l.a.createElement("div",{className:"site-wrapper user-cabinet"},l.a.createElement("nav",{className:"gov-nav"},l.a.createElement("div",{className:"wrapper"},l.a.createElement("div",{className:"subnav"},"\u0414\u0440\u0443\u0433\u0438\u0435 \u0441\u0430\u0439\u0442\u044b \u0440\u0435\u0441\u043f\u0443\u0431\u043b\u0438\u043a\u0438"),l.a.createElement("div",{className:"spacer"}),l.a.createElement("div",{className:"translate-menu"},"Rissian"),l.a.createElement("div",{className:"auth"},"\u041b\u0438\u0447\u043d\u044b\u0439 \u043a\u0430\u0431\u0438\u043d\u0435\u0442"))),l.a.createElement("div",{className:"top-part"},l.a.createElement("div",{className:"wrapper"},l.a.createElement("header",{className:"site-header"},l.a.createElement(m.b,{className:"logo",to:"/"},l.a.createElement("div",{className:"prime-text"},"\u0413\u043e\u0441\u0443\u0434\u0430\u0440\u0441\u0442\u0432\u0435\u043d\u043d\u044b\u0435 \u0443\u0441\u043b\u0443\u0433\u0438 ",l.a.createElement("br",null),l.a.createElement("span",null,"\u0420\u0435\u0441\u043f\u0443\u0431\u043b\u0438\u043a\u0438 \u0422\u0430\u0442\u0430\u0440\u0441\u0442\u0430\u043d"))),l.a.createElement("ul",{className:"help-nav"},l.a.createElement("li",null,l.a.createElement(m.b,{to:"/"},"\u041a\u0430\u0442\u0430\u043b\u043e\u0433 \u0443\u0441\u043b\u0443\u0433")),l.a.createElement("li",null,l.a.createElement(m.b,{to:"/"},"\u041f\u043e\u043c\u043e\u0449\u044c \u0438 \u043f\u043e\u0434\u0434\u0435\u0440\u0436\u043a\u0430")),l.a.createElement("li",null,l.a.createElement(m.b,{to:"/"},"\u041e\u043f\u043b\u0430\u0442\u0430")))))),l.a.createElement("div",{className:"bottom-part"},l.a.createElement("div",{className:"wrapper"},l.a.createElement("h1",null,"\u041b\u0438\u0447\u043d\u044b\u0439 \u043a\u0430\u0431\u0438\u043d\u0435\u0442 \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f"),l.a.createElement(F.a,{tabs:!0},l.a.createElement(O.a,null,l.a.createElement(C.a,{className:S()({active:"1"===this.state.activeTab}),onClick:function(){e.toggle("1")}},"\u041f\u0435\u0440\u0441\u043e\u043d\u0430\u043b\u044c\u043d\u044b\u0435 \u0434\u0430\u043d\u043d\u044b\u0435")),l.a.createElement(O.a,null,l.a.createElement(C.a,{className:S()({active:"2"===this.state.activeTab}),onClick:function(){e.toggle("2")}},"\u0412\u0430\u0448\u0438 \u0437\u0430\u044f\u0432\u043a\u0438"))),l.a.createElement(j.a,{activeTab:this.state.activeTab},l.a.createElement(w.a,{tabId:"1"},l.a.createElement(k.a,null,l.a.createElement(_.a,{md:"4"},l.a.createElement(x.a,null,l.a.createElement(E.a,{for:"second-name-control"},"\u0424\u0430\u043c\u0438\u043b\u0438\u044f"),l.a.createElement(p.a,{type:"text",name:"second-name-control",id:"second-name-control",value:this.state.formFields.last_name,onChange:function(a){return e.handleChangeField(a,"last_name")}}))),l.a.createElement(_.a,{md:"4"},l.a.createElement(x.a,null,l.a.createElement(E.a,{for:"name-control"},"\u0418\u043c\u044f"),l.a.createElement(p.a,{type:"text",name:"name-control",id:"name-control",value:this.state.formFields.first_name,onChange:function(a){return e.handleChangeField(a,"first_name")}}))),l.a.createElement(_.a,{md:"4"},l.a.createElement(x.a,null,l.a.createElement(E.a,{for:"father-name-control"},"\u041e\u0442\u0447\u0435\u0441\u0442\u0432\u043e"),l.a.createElement(p.a,{type:"text",name:"father-name-control",id:"father-name-control",value:this.state.formFields.father_name,onChange:function(a){return e.handleChangeField(a,"father_name")}})))),l.a.createElement(k.a,null,l.a.createElement(_.a,{md:"4"},l.a.createElement(x.a,null,l.a.createElement(E.a,{for:"email-control"},"E-mail"),l.a.createElement(p.a,{type:"email",name:"email-control",id:"email-control",value:this.state.formFields.email,onChange:function(a){return e.handleChangeField(a,"email")}}))),l.a.createElement(_.a,{md:"4"},l.a.createElement(x.a,null,l.a.createElement(E.a,{for:"phone-control"},"\u0422\u0435\u043b\u0435\u0444\u043e\u043d"),l.a.createElement(p.a,{type:"phone",name:"phone-control",id:"phone-control",value:this.state.formFields.phone,onChange:function(a){return e.handleChangeField(a,"phone")}})))),l.a.createElement(k.a,null,l.a.createElement(_.a,{md:"4"},l.a.createElement(x.a,null,l.a.createElement(E.a,{for:"inn-control"},"\u0418\u041d\u041d"),l.a.createElement(p.a,{type:"text",name:"inn-control",id:"inn-control",value:this.state.formFields.inn,onChange:function(a){return e.handleChangeField(a,"inn")}}))),l.a.createElement(_.a,{md:"4"},l.a.createElement(x.a,null,l.a.createElement(E.a,{for:"snils-control"},"\u0421\u041d\u0418\u041b\u0421"),l.a.createElement(p.a,{type:"text",name:"snils-control",id:"snils-control",value:this.state.formFields.snils,onChange:function(a){return e.handleChangeField(a,"snils")}}))),l.a.createElement(_.a,{md:"4"},l.a.createElement(x.a,null,l.a.createElement(E.a,{for:"passport-control"},"\u0421\u0435\u0440\u0438\u044f \u0438 \u043d\u043e\u043c\u0435\u0440 \u043f\u0430\u0441\u043f\u043e\u0440\u0442\u0430"),l.a.createElement(p.a,{type:"text",name:"passport-control",id:"passport-control",value:this.state.formFields.passport,onChange:function(a){return e.handleChangeField(a,"passport")}})))),l.a.createElement("div",{className:"form-actions"},l.a.createElement(v.a,null,"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c"))),l.a.createElement(w.a,{tabId:"2"},function(e){var a=e.map((function(e){return l.a.createElement("div",{key:e.id.toString(),className:"item ".concat(e.status&&"\u041f\u0440\u0438\u043d\u044f\u0442\u0430"===e.status?"status-accepted":"").concat(e.status&&"\u0412 \u0440\u0430\u0431\u043e\u0442\u0435"===e.status?"status-wip":"").concat(e.status&&"\u0412\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u0430"===e.status?"status-complete":"").concat(e.status&&"\u041e\u0442\u043a\u043b\u043e\u043d\u0435\u043d\u0430"===e.status?"status-rejected":"")},l.a.createElement("div",{className:"item-name"},e.name),e.status&&l.a.createElement("div",{className:"item-status"},"\u0421\u0442\u0430\u0442\u0443\u0441 \u0437\u0430\u044f\u0432\u043a\u0438: ",e.status),e.publish_date&&l.a.createElement("div",{className:"item-publish-date"},l.a.createElement("strong",null,"\u0414\u0430\u0442\u0430 \u043f\u043e\u0434\u0430\u0447\u0438 \u0437\u0430\u044f\u0432\u043a\u0438:")," ",e.publish_date),e.eliminate_days&&l.a.createElement("div",{className:"item-estimates"},l.a.createElement("strong",null,"\u0421\u0440\u043e\u043a\u0438 \u043e\u043a\u0430\u0437\u0430\u043d\u0438\u044f \u0443\u0441\u043b\u0443\u0433\u0438:")," ",e.eliminate_days," ",R(e.eliminate_days,"\u0434\u0435\u043d\u044c","\u0434\u043d\u044f","\u0434\u043d\u0435\u0439")),e.complete_date&&l.a.createElement("div",{className:"item-complition-date"},l.a.createElement("strong",null,"\u0414\u0430\u0442\u0430 \u0432\u044b\u043d\u0435\u0441\u0435\u043d\u0438\u044f \u0440\u0435\u0448\u0435\u043d\u0438\u044f:")," ",e.complete_date))}));return a.length>0?l.a.createElement("div",{className:"service-request-list"},a):l.a.createElement("div",{className:"service-request-list"},l.a.createElement("div",null,"\u041d\u0435\u0442 \u0430\u043a\u0442\u0438\u0432\u043d\u044b\u0445 \u0437\u0430\u044f\u0432\u043e\u043a"))}(a))))))}}]),a}(n.Component);function L(e,a){var t=Object.keys(e);if(Object.getOwnPropertySymbols){var n=Object.getOwnPropertySymbols(e);a&&(n=n.filter((function(a){return Object.getOwnPropertyDescriptor(e,a).enumerable}))),t.push.apply(t,n)}return t}function M(e){for(var a=1;a<arguments.length;a++){var t=null!=arguments[a]?arguments[a]:{};a%2?L(t,!0).forEach((function(a){Object(y.a)(e,a,t[a])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(t)):L(t).forEach((function(a){Object.defineProperty(e,a,Object.getOwnPropertyDescriptor(t,a))}))}return e}var B=function(e){function a(e){var t;return Object(o.a)(this,a),(t=Object(u.a)(this,Object(d.a)(a).call(this,e))).state={formFields:{}},t.handleChangeField=t.handleChangeField.bind(Object(N.a)(t)),t.handleFormSubmit=t.handleFormSubmit.bind(Object(N.a)(t)),t}return Object(h.a)(a,e),Object(i.a)(a,[{key:"handleChangeField",value:function(e,a){var t=this.state.formFields;this.setState({formFields:M({},t,Object(y.a)({},a,M({},t[a],{value:e.target.value})))})}},{key:"componentDidMount",value:function(){var e=this,a=this.props.match;g.a.get("/api/template?hash=hv123&id=".concat(a.params.id)).then((function(a){200===a.status&&e.setState({formFields:a.data?a.data:{}})}))}},{key:"handleFormSubmit",value:function(){var e=this.props.match,a={},t=this.state.formFields;for(var n in t)a=M({},a,{},Object(y.a)({},n,t[n].value));g.a.post("/api/setrequest?hash=hv123",M({},a,{type:e.params.id})).then((function(){window.location.href="https://digital.codedream.ru/#/"}))}},{key:"render",value:function(){var e=this,a=this.state.formFields,t=["first_name","last_name","father_name","phone","email","region","rajon","street","house","apartment","korpus"],r=Object.keys(a).filter((function(e){return!t.includes(e)})).reduce((function(e,t){return e[t]=a[t],e}),{});return l.a.createElement("div",{className:"site-wrapper service-request-page"},l.a.createElement("nav",{className:"gov-nav"},l.a.createElement("div",{className:"wrapper"},l.a.createElement("div",{className:"subnav"},"\u0414\u0440\u0443\u0433\u0438\u0435 \u0441\u0430\u0439\u0442\u044b \u0440\u0435\u0441\u043f\u0443\u0431\u043b\u0438\u043a\u0438"),l.a.createElement("div",{className:"spacer"}),l.a.createElement("div",{className:"translate-menu"},"Rissian"),l.a.createElement(m.b,{to:"/cabinet",className:"auth"},"\u041b\u0438\u0447\u043d\u044b\u0439 \u043a\u0430\u0431\u0438\u043d\u0435\u0442"))),l.a.createElement("div",{className:"top-part"},l.a.createElement("div",{className:"wrapper"},l.a.createElement("header",{className:"site-header"},l.a.createElement(m.b,{className:"logo",to:"/"},l.a.createElement("div",{className:"prime-text"},"\u0413\u043e\u0441\u0443\u0434\u0430\u0440\u0441\u0442\u0432\u0435\u043d\u043d\u044b\u0435 \u0443\u0441\u043b\u0443\u0433\u0438 ",l.a.createElement("br",null),l.a.createElement("span",null,"\u0420\u0435\u0441\u043f\u0443\u0431\u043b\u0438\u043a\u0438 \u0422\u0430\u0442\u0430\u0440\u0441\u0442\u0430\u043d"))),l.a.createElement("ul",{className:"help-nav"},l.a.createElement("li",null,l.a.createElement(m.b,{to:"/"},"\u041a\u0430\u0442\u0430\u043b\u043e\u0433 \u0443\u0441\u043b\u0443\u0433")),l.a.createElement("li",null,l.a.createElement(m.b,{to:"/"},"\u041f\u043e\u043c\u043e\u0449\u044c \u0438 \u043f\u043e\u0434\u0434\u0435\u0440\u0436\u043a\u0430")),l.a.createElement("li",null,l.a.createElement(m.b,{to:"/"},"\u041e\u043f\u043b\u0430\u0442\u0430")))))),l.a.createElement("div",{className:"bottom-part"},l.a.createElement("div",{className:"wrapper"},l.a.createElement("h1",null,"\u0412\u044b\u0434\u0430\u0447\u0430 \u0437\u0430\u044f\u0432\u043b\u0435\u043d\u0438\u044f \u043d\u0430 \u0441\u0442\u0440\u043e\u0438\u0442\u0435\u043b\u044c\u0441\u0442\u0432\u043e"),0!==Object.keys(a).length&&l.a.createElement(n.Fragment,null,l.a.createElement("h3",null,"\u0412\u0430\u0448\u0438 \u043f\u0435\u0440\u0441\u043e\u043d\u0430\u043b\u044c\u043d\u044b\u0435 \u0434\u0430\u043d\u043d\u044b\u0435"),l.a.createElement(k.a,null,l.a.createElement(_.a,{md:"4"},l.a.createElement(x.a,null,l.a.createElement(E.a,{for:"last-name-control"},"\u0424\u0430\u043c\u0438\u043b\u0438\u044f"),l.a.createElement(p.a,{type:"text",name:"last-name-control",id:"last-name-control",value:this.state.formFields.last_name.value,onChange:function(a){return e.handleChangeField(a,"last_name")}}))),l.a.createElement(_.a,{md:"4"},l.a.createElement(x.a,null,l.a.createElement(E.a,{for:"name-control"},"\u0418\u043c\u044f"),l.a.createElement(p.a,{type:"text",name:"name-control",id:"name-control",value:this.state.formFields.first_name.value,onChange:function(a){return e.handleChangeField(a,"first_name")}}))),l.a.createElement(_.a,{md:"4"},l.a.createElement(x.a,null,l.a.createElement(E.a,{for:"father-name-control"},"\u041e\u0442\u0447\u0435\u0441\u0442\u0432\u043e"),l.a.createElement(p.a,{type:"text",name:"father-name-control",id:"father-name-control",value:this.state.formFields.father_name.value,onChange:function(a){return e.handleChangeField(a,"father_name")}})))),l.a.createElement(k.a,null,l.a.createElement(_.a,{md:"4"},l.a.createElement(x.a,null,l.a.createElement(E.a,{for:"phone-control"},"\u041a\u043e\u043d\u0442\u0430\u043a\u0442\u043d\u044b\u0439 \u0442\u0435\u043b\u0435\u0444\u043e\u043d"),l.a.createElement(p.a,{type:"phone",name:"phone-control",id:"phone-control",value:this.state.formFields.phone.value,onChange:function(a){return e.handleChangeField(a,"phone")}}))),l.a.createElement(_.a,{md:"4"},l.a.createElement(x.a,null,l.a.createElement(E.a,{for:"email-control"},"E-mail"),l.a.createElement(p.a,{type:"email",name:"email-control",id:"email-control",value:this.state.formFields.email.value,onChange:function(a){return e.handleChangeField(a,"email")}})))),l.a.createElement("h3",null,"\u0410\u0434\u0440\u0435\u0441 \u043c\u0435\u0441\u0442\u0430 \u043f\u0440\u0435\u0431\u044b\u0432\u0430\u043d\u0438\u044f"),l.a.createElement(k.a,null,l.a.createElement(_.a,{md:"4"},l.a.createElement(x.a,null,l.a.createElement(E.a,{for:"region-control"},"\u0420\u0435\u0433\u0438\u043e\u043d"),l.a.createElement(p.a,{type:"text",name:"region-control",id:"region-control",value:this.state.formFields.region.value,onChange:function(a){return e.handleChangeField(a,"region")}}))),l.a.createElement(_.a,{md:"4"},l.a.createElement(x.a,null,l.a.createElement(E.a,{for:"rayon-control"},"\u0420\u0430\u0439\u043e\u043d"),l.a.createElement(p.a,{type:"text",name:"rayon-control",id:"rayon-control",value:this.state.formFields.rajon.value,onChange:function(a){return e.handleChangeField(a,"rajon")}}))),l.a.createElement(_.a,{md:"4"},l.a.createElement(x.a,null,l.a.createElement(E.a,{for:"street-control"},"\u0423\u043b\u0438\u0446\u0430"),l.a.createElement(p.a,{type:"text",name:"street-control",id:"street-control",value:this.state.formFields.street.value,onChange:function(a){return e.handleChangeField(a,"street")}})))),l.a.createElement(k.a,null,l.a.createElement(_.a,{md:"4"},l.a.createElement(x.a,null,l.a.createElement(E.a,{for:"house-control"},"\u0414\u043e\u043c"),l.a.createElement(p.a,{type:"text",name:"house-control",id:"house-control",value:this.state.formFields.house.value,onChange:function(a){return e.handleChangeField(a,"house")}}))),l.a.createElement(_.a,{md:"4"},l.a.createElement(x.a,null,l.a.createElement(E.a,{for:"apartment-control"},"\u041a\u0432\u0430\u0440\u0442\u0438\u0440\u0430"),l.a.createElement(p.a,{type:"text",name:"apartment-control",id:"apartment-control",value:this.state.formFields.apartment.value,onChange:function(a){return e.handleChangeField(a,"apartment")}}))),l.a.createElement(_.a,{md:"4"},l.a.createElement(x.a,null,l.a.createElement(E.a,{for:"korpus-control"},"\u041a\u043e\u0440\u043f\u0443\u0441"),l.a.createElement(p.a,{type:"text",name:"korpus-control",id:"korpus-control",value:this.state.formFields.korpus.value,onChange:function(a){return e.handleChangeField(a,"korpus")}}))))),0!==Object.keys(r).length&&function(a){var t=[],r=function(r){switch(a[r].type){case"fileupload":t.push(l.a.createElement(n.Fragment,{key:"".concat(a[r].type,"-").concat(a[r].key)},l.a.createElement("h3",null,a[r].label),l.a.createElement("div",{className:"drop-loader"},"\u041f\u0435\u0440\u0435\u0442\u0430\u0449\u0438\u0442\u0435 \u0444\u0430\u0439\u043b\u044b \u0441\u044e\u0434\u0430 \u0438\u043b\u0438 ",l.a.createElement("label",{htmlFor:"drop-loader"},"\u0437\u0430\u0433\u0440\u0443\u0437\u0438\u0442\u0435 \u0432\u0440\u0443\u0447\u043d\u0443\u044e"),l.a.createElement("input",{type:"file",name:"drop-loader",id:"drop-loader"}))));break;case"text":t.push(l.a.createElement(k.a,null,l.a.createElement(_.a,{lg:"4"},l.a.createElement(x.a,null,l.a.createElement(E.a,{for:"".concat(a[r].key,"-").concat(a[r].type)},a[r].label),l.a.createElement(p.a,{type:"text",name:"".concat(a[r].key,"-").concat(a[r].type),id:"".concat(a[r].key,"-").concat(a[r].type),value:e.state.formFields[r].value,onChange:function(a){return e.handleChangeField(a,r)}})))));break;default:t.push(l.a.createElement(n.Fragment,{key:"".concat(a[r].type,"-").concat(a[r].key)}))}};for(var c in a)r(c);return t.length>0?l.a.createElement(n.Fragment,null,t):l.a.createElement(n.Fragment,null)}(r),(0!==Object.keys(r).length||0!==Object.keys(a).length)&&l.a.createElement("div",{className:"form-actions"},l.a.createElement(v.a,{onClick:this.handleFormSubmit},"\u041e\u0442\u043f\u0440\u0430\u0432\u0438\u0442\u044c")))))}}]),a}(n.Component);var J=function(){return l.a.createElement(m.a,null,l.a.createElement(s.c,null,l.a.createElement(s.a,{path:"/",exact:!0,component:b}),l.a.createElement(s.a,{path:"/cabinet",exact:!0,component:I}),l.a.createElement(s.a,{path:"/service-request/:id",exact:!0,component:B})))};Boolean("localhost"===window.location.hostname||"[::1]"===window.location.hostname||window.location.hostname.match(/^127(?:\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)){3}$/));c.a.render(l.a.createElement(J,null),document.getElementById("root")),"serviceWorker"in navigator&&navigator.serviceWorker.ready.then((function(e){e.unregister()}))}},[[43,1,2]]]);
//# sourceMappingURL=main.a1515de9.chunk.js.map